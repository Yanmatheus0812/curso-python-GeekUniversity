from classe import Produto, Mercado, Carrinho
import os

def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def enter_para_continuar():
    input("Pressione enter para continuar...")

mercado = Mercado()
carrinho = Carrinho()

print("Bem-vindo ao mercado, o que deseja fazer?")

print("1- entrar como admin")
print("2- entrar como cliente")
escolha: int = int(input("digite a opcao: "))

if escolha == 1:
    senha: str = input("digite a senha para entrar: ")

    if senha == "senha123":
        while True:
            limpar_terminal()
            print("1- cadastrar produto")
            print("2- excluir produto")
            print("3- visualizar produtos")
            print("0- sair")
            escolha = int(input("digite a opcao: "))
        
            if escolha == 0:
                print("saindo do programa...")
                exit()

            elif escolha == 1:
                nome: str = input("digite o nome do produto: ")
                preco: float = input("digite o preco do produto, R$: ")
                produto = Produto(nome, preco)
                mercado.cadastrar_produtos(produto)
                enter_para_continuar()
            
            elif escolha == 2:
                nome: str = input("digite o nome do produto que deseja excluir: ")
                mercado.excluir_produtos(nome)
                enter_para_continuar()
            
            elif escolha == 3:
                mercado.visualizar_produtos()
                enter_para_continuar()

    
    else:
        print("Senha incorreta")
        exit()

elif escolha == 2:
    while True:
        limpar_terminal()
        print("1- visualizar produtos")
        print("2- ver meu carrinho")
        print("3- adicionar produto ao carrinho")
        print("4- remover produto do carrinho")
        print("5- finalizar compra")
        print("0- sair")
        escolha = int(input("digite a opcao: "))

        if escolha == 0:
            print("saindo do programa...")
            exit()
        
        elif escolha == 1:
            mercado.visualizar_produtos()
            enter_para_continuar()
        
        elif escolha == 2:
            carrinho.visualizar_carrinho()
            enter_para_continuar()

        elif escolha == 3:
            nome: str = input("digite o nome do produto: ")
            quantidade: int = int(input("Digite a quantidade que deseja adicionar ao carrinho: "))
            carrinho.adicionar_carrinho(nome, quantidade)
            enter_para_continuar()

        elif escolha == 4:
            nome: str = input("digite o nome do produto que deseja remover do carrinho: ")
            carrinho.excluir_carrinho(nome)
            enter_para_continuar()

        elif escolha == 5:
            valor = carrinho.comprar()
            print(f"o valor total do seu carrinho foi de R${valor}, obrigado e volte sempre!")
            exit()
