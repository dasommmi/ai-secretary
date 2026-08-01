from datetime import date

from ai.openrouter import ask_openrouter
from domain.knowledge.entities import KnowledgeItem, DailyDigest
from domain.knowledge.ports import KnowledgeCuratorPort


class OpenRouterKnowledgeCurator(KnowledgeCuratorPort):

    def curate(self, interests: list[str]) -> DailyDigest:

        prompt = self._build_prompt(interests)

        response = ask_openrouter(prompt)

        item = self._parse_response(response)

        return DailyDigest(digest_date=date.today(), items=[item])

    def _build_prompt(self, interests: list[str]) -> str:

        return f"""
너는 개인 지식 큐레이터야.

사용자의 관심 분야:
{interests}


오늘 알아두면 좋은 지식 1개를 만들어줘.


조건:

- 질문과 답변 형태
- 너무 뻔한 내용 금지
- 친구에게 설명할 수 있는 수준
- 재미있거나 실용적인 내용


형식:

QUESTION:
질문

ANSWER:
답변
"""

    def _parse_response(self, response: str) -> KnowledgeItem:

        question = ""
        answer = ""

        lines = response.split("\n")

        for line in lines:

            if line.startswith("QUESTION:"):

                question = line.replace("QUESTION:", "").strip()

            elif line.startswith("ANSWER:"):

                answer = line.replace("ANSWER:", "").strip()

        return KnowledgeItem(category="GENERAL", question=question, answer=answer)
