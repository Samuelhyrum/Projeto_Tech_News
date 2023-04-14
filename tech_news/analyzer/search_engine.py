from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    """Seu código deve vir aqui"""
    db_return = search_news({"title": {"$regex": title.lower()}})
    lista_tuplas = [(news["title"], news["url"]) for news in db_return]
    return lista_tuplas


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
