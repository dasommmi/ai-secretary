from datetime import date

from domain.knowledge.entities import DailyDigest
from domain.knowledge.ports import (
    InterestRepositoryPort,
    KnowledgeCuratorPort,
    DigestRepositoryPort,
)


class GenerateDailyDigestUseCase:

    def __init__(
        self,
        interest_repository: InterestRepositoryPort,
        digest_repository: DigestRepositoryPort,
        curator: KnowledgeCuratorPort,
    ):

        self.interest_repository = interest_repository
        self.digest_repository = digest_repository
        self.curator = curator

    # def execute(self) -> DailyDigest | None:
    #
    #     if self.digest_repository.exists_today():
    #
    #         print("오늘 Digest가 이미 생성되었습니다.")
    #
    #         return None
    #
    #     interests = self.interest_repository.find_all()
    #
    #     items = []
    #
    #     for category in interests:
    #
    #         item = self.curator.curate(category)
    #
    #         if self.digest_repository.exists_question(item.question):
    #             print("중복 Knowledge 제거:", item.question)
    #             continue
    #
    #         items.append(item)
    #
    #     digest = DailyDigest(digest_date=date.today(), items=items)
    #     print(digest.items)
    #     self.digest_repository.save(digest)
    #
    #     return digest

    def execute(self) -> DailyDigest | None:

        print("🔥 GenerateDailyDigest start")

        if self.digest_repository.exists_today():

            print("오늘 Digest가 이미 생성되었습니다.")

            return None

        interests = self.interest_repository.find_all()

        print("관심 카테고리:", interests)

        items = []

        for category in interests:

            print("생성 category:", category)

            item = self.curator.curate(category)

            print("생성 결과:", item.question)

            if self.digest_repository.exists_question(item.question):

                print("중복 Knowledge 제거:", item.question)

                continue

            items.append(item)

        print("최종 생성 개수:", len(items))

        digest = DailyDigest(digest_date=date.today(), items=items)

        self.digest_repository.save(digest)

        return digest
