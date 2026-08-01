from ai.openrouter import ask_openrouter
from domain.knowledge.category_profiles import CATEGORY_PROFILES
from domain.knowledge.entities import KnowledgeItem


class OpenRouterKnowledgeCurator:

    def curate(self, category: str) -> KnowledgeItem:

        profile = CATEGORY_PROFILES[category]

        prompt = self._build_prompt(profile)

        response = ask_openrouter(prompt)

        return self._parse_response(category, response)

    def _build_prompt(self, profile):

        return f"""
너는 개인 지식 큐레이터다.

카테고리:
{profile.description}


작성 규칙:

{profile.prompt_rule}


조건:

- 친구에게 설명하기 좋은 내용
- 너무 흔한 상식 금지
- 질문/답변 형식
- 하나의 주제만 선택


출력 형식:

QUESTION:
질문

ANSWER:
답변
"""

    def _parse_response(self, category, response):
        print("===== AI RESPONSE =====")

        print(response)

        print("======================")
        question = ""
        answer = ""

        mode = None

        for line in response.splitlines():

            line = line.strip()

            if not line:
                continue

            if line.upper().startswith("QUESTION"):

                mode = "question"

                content = line.split(":", 1)

                if len(content) > 1 and content[1].strip():

                    question = content[1].strip()

                continue

            if line.upper().startswith("ANSWER"):

                mode = "answer"

                content = line.split(":", 1)

                if len(content) > 1 and content[1].strip():

                    answer = content[1].strip()

                continue

            if mode == "question":

                question += " " + line

            elif mode == "answer":

                answer += " " + line

        return KnowledgeItem(
            category=category, question=question.strip(), answer=answer.strip()
        )
