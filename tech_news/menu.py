from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
import sys


def popular_banco():
    news_quantity = int(input("Digite quantas notícias serão buscadas: "))
    get_tech_news(news_quantity)
    print("Notícias adicionadas com sucesso!")


def buscar_por_titulo():
    title = input("Digite o título: ")
    result = search_by_title(title)
    print(result)


def buscar_por_data():
    date = input("Digite a data no formato aaaa-mm-dd: ")
    result = search_by_date(date)
    print(result)


def buscar_por_categoria():
    category = input("Digite a categoria: ")
    result = search_by_category(category)
    print(result)


def listar_top_categorias():
    result = top_5_categories()
    print("As 5 categorias mais populares são:")
    print(result)


def sair():
    print("Encerrando script")


# mapeamento das opções do menu aos métodos correspondentes
opcoes = {
    '0': popular_banco,
    '1': buscar_por_titulo,
    '2': buscar_por_data,
    '3': buscar_por_categoria,
    '4': listar_top_categorias,
    '5': sair
}


def analyzer_menu():

    print("Selecione uma das opções a seguir:")
    print(" 0 - Popular o banco com notícias;")
    print(" 1 - Buscar notícias por título;")
    print(" 2 - Buscar notícias por data;")
    print(" 3 - Buscar notícias por categoria;")
    print(" 4 - Listar top 5 categorias;")
    print(" 5 - Sair.")

    opcao = input("Digite o número da opção desejada: ")

    try:
        opcoes[opcao]()
    except KeyError:
        print("Opção inválida", file=sys.stderr)
