from datetime import date

from domain.knowledge.entities import DailyDigest
from domain.knowledge.ports import InterestRepositoryPort, KnowledgeCuratorPort


class GenerateDailyDigestUseCase:

    def __init__(
        self, interest_repository: InterestRepositoryPort, curator: KnowledgeCuratorPort
    ):

        self.interest_repository = interest_repository
        self.curator = curator

    def execute(self) -> DailyDigest:

        interests = self.interest_repository.find_all()

        items = []

        for category in interests:

            item = self.curator.curate(category)

            items.append(item)

        return DailyDigest(digest_date=date.today(), items=items)
