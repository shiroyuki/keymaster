from dataclasses import dataclass
from typing import List, Any, Dict, Optional

from keymaster.model.credential import Credential
from keymaster.model.note import Note


@dataclass
class DecryptedData:
    credentials: List[Credential]
    notes: List[Note]

    @staticmethod
    def make(raw_data: Optional[Dict[str, Any]] = None):
        if not raw_data:
            return DecryptedData(credentials=[], notes=[])

        return DecryptedData(
            credentials=[
                Credential(**item)
                for item in raw_data.get('credentials')
            ],
            notes=[
                Note(**item)
                for item in raw_data.get('notes')
            ],
        )
