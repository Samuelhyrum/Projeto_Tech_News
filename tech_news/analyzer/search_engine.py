from tech_news.database import search_news
from datetime import datetime


def lista_tuplas(lista):
    return [(news["title"], news["url"]) for news in lista]


# Requisito 7
def search_by_title(title):
    """Seu código deve vir aqui"""
    db_return = search_news({"title": {"$regex": title.lower()}})
    return lista_tuplas(db_return)


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        date_D_M_Y = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        db_return = search_news({"timestamp": date_D_M_Y})

        return lista_tuplas(db_return)
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
