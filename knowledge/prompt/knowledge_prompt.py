from knowledge.category import KnowledgeCategory


def build_knowledge_prompt(category: str):

    prompts = {
        KnowledgeCategory.TECH_AI.value: """
            개발자에게 도움이 되는 IT/AI 지식을 만들어줘.
    
            너무 기초적인 내용 말고,
            실제 개발자가 알아두면 좋은 내용을 선택해.
    
            질문과 답변 형태로 작성해.
            """,
        KnowledgeCategory.HOBBY.value: """
            취미와 관련된 흥미로운 지식을 만들어줘.
    
            커피, 사진, 음악, 악기, 운동 등
            일상에서 활용할 수 있는 내용이면 좋아.
    
            질문과 답변 형태로 작성해.
            """,
        KnowledgeCategory.GENERAL.value: """
            일상 교양 지식을 만들어줘.
    
            과학, 역사, 생활 상식, 요리 등
            알아두면 좋은 내용을 선택해.
    
            질문과 답변 형태로 작성해.
            """,
        KnowledgeCategory.FUN_TMI.value: """
            친구에게 이야기하기 좋은
            재미있는 TMI 지식을 만들어줘.
            넌센스 퀴즈도 좋아.
    
            놀랍거나 흥미로운 내용을 선택해.
    
            질문과 답변 형태로 작성해.
            """,
        KnowledgeCategory.MONEY_ECONOMY.value: """
            경제와 금융 관련 지식을 만들어줘.
    
            투자자가 알아두면 좋은
            개념들 위주로 작성해.
            
            그리고 금융 상품 관련 쪽도 좋아.
    
            질문과 답변 형태로 작성해.
            """,
    }

    return prompts[category]
