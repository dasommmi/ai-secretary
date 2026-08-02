from dataclasses import dataclass
from datetime import date


@dataclass
class KnowledgeItem:

    category: str

    question: str

    answer: str

    source: str = "AI"


@dataclass
class DailyDigest:

    digest_date: date

    items: list[KnowledgeItem]
