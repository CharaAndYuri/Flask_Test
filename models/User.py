from dataclasses import dataclass, asdict


@dataclass
class User:
    id: int
    email: str
    name: str
    surname: str
    age: int
    city: str
    password: str

    def __dict__(self):
        return asdict(self)
