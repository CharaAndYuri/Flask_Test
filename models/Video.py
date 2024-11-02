from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Video:
    id: int | None
    user_id: int
    name: str
    filename: str

    def __dict__(self):
        return asdict(self)