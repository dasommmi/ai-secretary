from dataclasses import dataclass


@dataclass
class Course:

    name: str

    remain: int

    total: int

    status: str
