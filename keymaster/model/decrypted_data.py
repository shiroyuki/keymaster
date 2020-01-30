from dataclasses import dataclass
from typing import List

from keymaster.model.credential import Credential
from keymaster.model.note import Note


@dataclass
class DecryptedData:
    credentials: List[Credential]
    notes: List[Note]

    @staticmethod
    def make():
        return DecryptedData(credentials=[], notes=[])
