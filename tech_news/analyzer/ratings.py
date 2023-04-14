from tech_news.database import search_news
from collections import Counter


# Requisito 10
def top_5_categories():
    """Seu código deve vir aqui"""
    data = search_news({})

    lista_category = [news["category"] for news in data]

    without_duplicates = Counter(lista_category)

    ordered_words = sorted(
        without_duplicates.keys(), key=lambda category: (
            -without_duplicates[category], category))

    return ordered_words[:5]
