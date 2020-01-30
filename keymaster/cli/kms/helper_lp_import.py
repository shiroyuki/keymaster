import re
from argparse import ArgumentParser, Namespace
from dataclasses import dataclass
import csv
from typing import List

from gallium.interface import ICommand
from imagination.standalone import container

from keymaster.model.credential import Credential
from keymaster.model.decrypted_data import DecryptedData
from keymaster.model.note import Note
from keymaster.storage import StorageService


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

        data = DecryptedData.make()

        for row in rows:
            tags = [row.grouping] if row.grouping else []

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

        storage: StorageService = container.get(StorageService)
        # TODO Merge with existing data before saving
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
