from ai.openrouter import ask_openrouter
from domain.knowledge.entities import KnowledgeItem


class OpenRouterKnowledgeCurator:

    def curate(self, category: str) -> KnowledgeItem:

        prompt = self._build_prompt(category)

        response = ask_openrouter(prompt)

        return self._parse_response(category, response)

    def _build_prompt(self, category: str):

        return f"""
너는 개인 지식 큐레이터다.

카테고리:
{category}


오늘 알아두면 좋은 지식 하나를 만들어줘.


조건:

- 친구에게 설명하기 좋은 내용
- 너무 뻔한 상식 금지
- 질문/답변 형식


출력:


QUESTION:
내용


ANSWER:
내용
"""

    def _parse_response(self, category: str, response: str):

        question = ""
        answer = ""

        for line in response.split("\n"):

            if line.startswith("QUESTION:"):

                question = line.replace("QUESTION:", "").strip()

            if line.startswith("ANSWER:"):

                answer = line.replace("ANSWER:", "").strip()

        return KnowledgeItem(category=category, question=question, answer=answer)
