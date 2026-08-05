from domain.knowledge.category import KnowledgeCategory

COMMON_RULE = """

아래 규칙을 반드시 지켜.

[공통 규칙]

1.
반드시 한국어로만 작성한다.

2.
영어 용어를 사용할 경우
괄호 안에 한국어 설명을 함께 적는다.

예)

Kafka(분산 메시지 시스템)

Partition(데이터 분할 단위)

Cache(임시 저장 공간)

3.
Markdown 문법 사용 금지

#, ##, *, -, ``` 절대 사용하지 않는다.

4.
친구에게 설명하듯 자연스럽게 작성한다.

5.
답변은 3~5문장으로 작성한다.

6.
너무 어려운 용어는 쉬운 말로 다시 설명한다.

7.
답변 마지막에는

한 줄 정리:

를 추가한다.

8.
출력 형식은 반드시 아래 형식을 따른다.

QUESTION:
질문

ANSWER:
답변

"""


def build_knowledge_prompt(category: str):

    prompts = {
        KnowledgeCategory.TECH_AI.value: """
개발자에게 도움이 되는 IT/AI 지식을 만들어줘.

너무 기초적인 내용은 제외하고,

실무 개발자가 알아두면 좋은 내용을 선택해.

""",
        KnowledgeCategory.HOBBY.value: """
취미와 관련된 흥미로운 지식을 만들어줘.

커피, 사진, 음악, 악기, 운동 등

일상에서 활용할 수 있는 내용을 선택해.

""",
        KnowledgeCategory.GENERAL.value: """
일상 교양 지식을 만들어줘.

과학, 역사, 생활 상식, 요리 등

알아두면 도움이 되는 내용을 선택해.

""",
        KnowledgeCategory.FUN_TMI.value: """
친구에게 이야기하기 좋은

재미있는 TMI를 만들어줘.

넌센스 퀴즈도 좋다.

술자리에서 이야기하기 좋은 수준이면 된다.

""",
        KnowledgeCategory.MONEY_ECONOMY.value: """
경제와 금융 관련 지식을 만들어줘.

투자자가 알아두면 좋은

개념이나 금융상품,

경제 흐름 등을 쉽게 설명해줘.

""",
    }

    return prompts[category] + COMMON_RULE
