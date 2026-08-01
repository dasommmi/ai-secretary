from domain.knowledge.category_profile import CategoryProfile

CATEGORY_PROFILES = {
    "TECH_AI": CategoryProfile(
        category="TECH_AI",
        description="개발, AI, IT 기술",
        prompt_rule="""
- 개발자가 알아두면 좋은 내용
- 최신 기술 트렌드
- 원리를 이해할 수 있는 설명
- 너무 전문적이지 않게
""",
    ),
    "HOBBY": CategoryProfile(
        category="HOBBY",
        description="취미와 관심사",
        prompt_rule="""
- 커피, 사진, 운동, 음악, 여행 등
- 실제 생활에서 이야기하기 좋은 내용
- 재미와 배움을 동시에 제공
""",
    ),
    "GENERAL": CategoryProfile(
        category="GENERAL",
        description="일반 상식",
        prompt_rule="""
- 일상에서 궁금할 만한 주제
- 이유와 원리를 설명
- 알고 나면 흥미로운 내용
""",
    ),
    "FUN_TMI": CategoryProfile(
        category="FUN_TMI",
        description="재미있는 이야기",
        prompt_rule="""
- 친구에게 이야기하기 좋은 내용
- 의외성 있는 정보
- 가벼운 농담 소재
""",
    ),
    "MONEY_ECONOMY": CategoryProfile(
        category="MONEY_ECONOMY",
        description="경제와 돈",
        prompt_rule="""
- 투자자가 알아두면 좋은 개념
- 경제 원리 설명
- 뉴스 이해에 도움되는 내용
""",
    ),
}
