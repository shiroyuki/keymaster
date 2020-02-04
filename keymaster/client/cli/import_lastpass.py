import csv
import re
from argparse import ArgumentParser, Namespace
from dataclasses import dataclass
from time import time
from typing import List

from gallium.interface import ICommand
from imagination.standalone import container

from keymaster.common.model.credential import Credential
from keymaster.common.model.decrypted_data import DecryptedData
from keymaster.common.model.note import Note
from keymaster.client.service.storage import StorageService


class LastPassImport(ICommand):
    """Import the data from a LastPass CSV file"""

    def identifier(self):
        return 'import:lastpass'

    def define(self, parser: ArgumentParser):
        parser.add_argument('export_file_path')

    def execute(self, args: Namespace):
        print(f'Importing from {args.export_file_path}...')

        rows: List[ExportedEntry] = []

        with open(args.export_file_path, 'r') as f:
            reader = csv.reader(f)
            read_header = False
            headers = []

            for row in reader:
                if not read_header:
                    read_header = True
                    headers.extend(row)
                    continue

                if not row:
                    continue

                rows.append(ExportedEntry(**{
                    headers[i]: row[i].strip()
                    for i in range(len(headers))
                }))

        storage: StorageService = container.get(StorageService)

        data = storage.load()
        default_tag = f'imported:{time()}'

        for row in rows:
            tags = [default_tag]

            if row.grouping:
                tags.append(row.grouping)

            if row.url == 'http://sn':
                data.notes.append(Note.make(row.name, row.extra, tags))
            else:
                if row.url == 'http://':
                    tags.append('local')
                else:
                    tags.append('web')
                    if re.search(r'^http://\d+(\.\d+){3}', row.url):
                        tags.append('intranet')
                    else:
                        tags.append('internet')
                data.credentials.append(Credential.make(row.name, row.username, row.password, row.extra, tags))
        storage.save(data)


@dataclass(frozen=True)
class ExportedEntry:
    url: str
    username: str
    password: str
    extra: str
    name: str
    grouping: str
    fav: str
