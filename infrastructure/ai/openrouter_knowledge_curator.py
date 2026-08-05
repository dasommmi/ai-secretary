from infrastructure.ai.openrouter import ask_openrouter

from domain.knowledge.category_profiles import CATEGORY_PROFILES
from domain.knowledge.entities import KnowledgeItem


class OpenRouterKnowledgeCurator:

    def curate(self, category: str) -> KnowledgeItem:

        profile = CATEGORY_PROFILES[category]

        for _ in range(3):

            prompt = self._build_prompt(profile)

            response = ask_openrouter(prompt)

            response = self._clean_response(response)

            if self._validate_response(response):

                return self._parse_response(category, response)

        raise Exception("Knowledge 생성 실패")

    def _build_prompt(self, profile):

        return f"""
너는 개인 지식 큐레이터다.

카테고리:
{profile.description}


작성 규칙:

{profile.prompt_rule}


추가 규칙:

- 반드시 한국어로 작성
- 영어 용어는 한국어 설명을 함께 작성
- Markdown 사용 금지
- #, -, *, **, ``` 사용 금지
- 친구에게 설명하듯 자연스럽게 작성
- 너무 어려운 용어는 쉽게 풀어서 설명
- 답변은 3~5문장
- 마지막에 "한 줄 정리:" 추가


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

    def _clean_response(self, response: str):

        response = response.replace("**", "").replace("```", "").replace("#", "")

        lines = []

        for line in response.splitlines():

            line = line.strip()

            if line:

                lines.append(line)

        return "\n".join(lines)

    def _validate_response(self, response: str):

        if "QUESTION:" not in response.upper():

            return False

        if "ANSWER:" not in response.upper():

            return False

        if len(response) < 100:

            return False

        return True

    def _parse_response(self, category, response):

        print("===== AI RESPONSE =====")

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

                if len(content) > 1:

                    question = content[1].strip()

                continue

            if line.upper().startswith("ANSWER"):

                mode = "answer"

                content = line.split(":", 1)

                if len(content) > 1:

                    answer = content[1].strip()

                continue

            if mode == "question":

                question += " " + line

            elif mode == "answer":

                answer += " " + line

        return KnowledgeItem(
            category=category, question=question.strip(), answer=answer.strip()
        )
