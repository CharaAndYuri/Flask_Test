from dataclasses import dataclass


@dataclass
class Link:
    name: str
    url: str
    icon: str | None = None
    class_name: str | None = None