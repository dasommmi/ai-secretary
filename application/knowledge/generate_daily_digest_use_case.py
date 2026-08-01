from domain.knowledge.entities import DailyDigest
from domain.knowledge.ports import KnowledgeCuratorPort


class GenerateDailyDigestUseCase:

    def __init__(self, curator: KnowledgeCuratorPort):

        self.curator = curator

    def execute(self, interests: list[str]) -> DailyDigest:

        return self.curator.curate(interests)
