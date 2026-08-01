from datetime import date

from domain.knowledge.entities import DailyDigest
from domain.knowledge.ports import KnowledgeCuratorPort


class GenerateDailyDigestUseCase:

    def __init__(self, curator: KnowledgeCuratorPort):

        self.curator = curator

    def execute(self, interests: list[str]) -> DailyDigest:

        items = []

        for category in interests:

            item = self.curator.curate(category)

            items.append(item)

        return DailyDigest(digest_date=date.today(), items=items)
