CATEGORY_DISPLAY_NAME = {
    "TECH_AI": "🤖 Tech & AI",
    "HOBBY": "🎸 Hobby",
    "GENERAL": "📚 General",
    "FUN": "😂 Fun / TMI",
    "MONEY": "💰 Money / Economy",
}


def get_category_name(category: str):

    return CATEGORY_DISPLAY_NAME.get(category, category)
