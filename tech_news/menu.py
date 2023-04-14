import sys


# Requisitos 11 e 12
def analyzer_menu():
    """Seu código deve vir aqui"""
    print("Selecione uma das opções a seguir:")
    print(" 0 - Popular o banco com notícias;")
    print(" 1 - Buscar notícias por título;")
    print(" 2 - Buscar notícias por data;")
    print(" 3 - Buscar notícias por categoria;")
    print(" 4 - Listar top 5 categorias;")
    print(" 5 - Sair.")

    opcao = input()

    if opcao == "0":
        print("Digite quantas notícias serão buscadas:")
    elif opcao == "1":
        print("Digite o título:")
    elif opcao == "2":
        print("Digite a data no formato aaaa-mm-dd:")
    elif opcao == "3":
        print("Digite a categoria:")
    elif opcao == "4":
        print("Listando top 5 categorias:")
    elif opcao == "5":
        print("Saindo do programa...")
    else:
        print("Opção inválida.", file=sys.stderr)
