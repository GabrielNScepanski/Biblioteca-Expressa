import os


livros = [
    {"titulo": "O Velho e o Mar", "autor": "Ernest Hemingway", "emprestado": False},
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "emprestado": True},
    {"titulo": "A Metamorfose", "autor": "Franz Kafka", "emprestado": False},
    {"titulo": "O Estrangeiro", "autor": "Albert Camus", "emprestado": True},
    {"titulo": "Sapiens ", "autor": "Yuval Harari", "emprestado": False}
]


def voltar_ao_menu_principal():
    input("\nPressione qualquer tecla para voltar ao menu principal: \n")
    main()


def mostrar_subtitulo(texto):
    os.system("clear")
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)


def desligar_app():
    mostrar_subtitulo("Encerrando o aplicativo")


def opcao_invalida():
    print("Opção inválida\n")
    voltar_ao_menu_principal()


def adicionar_novo_livro():
    os.system("clear")
    titulo_do_livro = input("Digite o título do novo livro: \n")
    autor_do_livro = input("Digite o autor do livro: \n")
    livros.append({"titulo": titulo_do_livro, "autor": autor_do_livro, "emprestado": False})
    print(f"\nO livro '{titulo_do_livro}' foi adicionado com sucesso!")
    voltar_ao_menu_principal()


def listar_livros():
    os.system("clear")
    print(f"{'Título'.ljust(30)} -- {'Autor'.ljust(20)} -- {'Status'}")
    for livro in livros:
        titulo = livro["titulo"].ljust(30)
        autor = livro["autor"].ljust(20)
        status = 'Disponível' if not livro['emprestado'] else 'Emprestado'
        print(f"- {titulo} -- {autor} -- {status}")
    voltar_ao_menu_principal()


def atualizar_status_livro():
    mostrar_subtitulo("Atualizando o status de empréstimo do livro")
    titulo_livro = input("Digite o título do livro que deseja atualizar o status: ")
    livro_encontrado = False
    for livro in livros:
        if titulo_livro == livro["titulo"]:
            livro_encontrado = True
            livro["emprestado"] = not livro["emprestado"]
            mensagem = f"O livro '{titulo_livro}' agora está disponível!" if not livro["emprestado"] else f"O livro '{titulo_livro}' agora está emprestado!"
            print(mensagem)
            break

    if not livro_encontrado:
        print("Livro não encontrado")
    voltar_ao_menu_principal()


def nome_app():
    print('''
𝕭𝖎𝖇𝖑𝖎𝖔𝖙𝖊𝖈𝖆 𝕰𝖝𝖕𝖗𝖊𝖘𝖘𝖆
''')


def exibir_opcoes():
    print("1 - Adicionar um novo livro")
    print("2 - Listar livros")
    print("3 - Atualizar status de empréstimo de um livro")
    print("4 - Sair do programa\n")


def escolher_opcoes():
    try:
        escolha = int(input("Escolha uma opção: "))
        print("Você selecionou a opção:", escolha, "\n")
        if escolha == 1:
            adicionar_novo_livro()
        elif escolha == 2:
            listar_livros()
        elif escolha == 3:
            atualizar_status_livro()
        elif escolha == 4:
            desligar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()


def main():
    os.system("clear")
    nome_app()
    exibir_opcoes()
    escolher_opcoes()


if __name__ == "__main__":
    main()