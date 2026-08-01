from typing import Protocol

from domain.knowledge.entities import KnowledgeItem, DailyDigest


class KnowledgeCuratorPort(Protocol):

    def curate(self, category: str) -> KnowledgeItem: ...


class DigestRepositoryPort(Protocol):

    def save(self, digest: DailyDigest): ...

    def exists_today(self) -> bool: ...


class InterestRepositoryPort(Protocol):

    def save(self, category: str): ...

    def find_all(self) -> list[str]: ...
