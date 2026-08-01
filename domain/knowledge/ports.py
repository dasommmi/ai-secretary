from typing import Protocol

from domain.knowledge.entities import DailyDigest


class KnowledgeCuratorPort(Protocol):

    def curate(self, interests: list[str]) -> DailyDigest: ...


class DigestRepositoryPort(Protocol):

    def save(self, digest: DailyDigest): ...

    def exists_today(self) -> bool: ...


class InterestRepositoryPort(Protocol):

    def save(self, interests: list[str]): ...

    def find(self) -> list[str]: ...
