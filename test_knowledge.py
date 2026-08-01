from knowledge.category import KnowledgeCategory
from knowledge.knowledge_service import KnowledgeService

service = KnowledgeService()


result = service.generate(KnowledgeCategory.TECH_AI.value)


print(result)
