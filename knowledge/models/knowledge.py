from dataclasses import dataclass
from datetime import datetime


@dataclass
class Knowledge:

    category: str

    question: str

    answer: str

    created_at: datetime = datetime.now()
