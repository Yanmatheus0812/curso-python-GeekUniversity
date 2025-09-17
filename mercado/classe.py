from csv import DictWriter, DictReader
caminho_lista_produtos: str = 'projetos/mercado/lista_produtos.csv'
caminho_carrinho: str = 'projetos/mercado/carrinho.csv'

# Classe produto
class Produto:
    __quantidade: int = 1

    def __init__(self: object, nome: str, preco: float):
        self.__nome: str = nome
        self.__preco: float = preco
    
    @property
    def nome(self: object) -> str:
        return self.__nome
    
    @property
    def preco(self: object) -> float:
        return self.__preco
    

class Mercado: 
    def __init__(self: object):
        pass


    def cadastrar_produtos(self: object, produto: Produto) -> None:
            with open(caminho_lista_produtos, 'a', newline='', encoding='utf-8') as lista:
                cabecalho = ['Nome', 'valor(R$)']
                escritor_csv = DictWriter(lista, fieldnames=cabecalho)
                escritor_csv.writerow({"Nome": produto.nome, "valor(R$)": produto.preco})


    def excluir_produtos(self: object, nome: str) -> None:
        '''
        Remove um produto da lista de produtos disponiveis, caso ele exista
        '''

        produtos_restantes: list = []
        produto_encontrado: bool = False

        # Lê a lista de produtos e verifica se o produto está presente
        with open(caminho_lista_produtos, 'r', encoding='utf-8') as lista:
            leitor_csv = DictReader(lista, delimiter=',')
            for linha in leitor_csv:
                if linha['Nome'].lower() != nome.lower():
                    produtos_restantes.append(linha)
                else:
                    produto_encontrado = True
        
        # reescreve a lista de produtos sem o produto removido
        if produto_encontrado:
            with open(caminho_lista_produtos, 'w', newline='', encoding='utf-8') as lista:
                cabecalho = ['Nome', 'valor(R$)']
                escritor_csv = DictWriter(lista, fieldnames=cabecalho)
                escritor_csv.writeheader()
                for produto in produtos_restantes:
                    escritor_csv.writerow(produto)
                print(f"{nome} excluido com sucesso!")
            
        else:
            print(f"{nome} nao encontrado")


    def visualizar_produtos(self: object) -> None:
        with open(caminho_lista_produtos, 'r', encoding='utf-8') as lista:
            leitor_csv = DictReader(lista, delimiter = ',')
            produtos = list(leitor_csv)

            if not produtos:
                print("Nenhum produto registrado")
            
            else:
                for linha in produtos:
                    print(f"{linha['Nome']} R${linha['valor(R$)']}")


class Carrinho():
    def __init__(self: object):
        pass

    
    def adicionar_carrinho(self: object, nome: str, quantidade: int) -> None:
        '''
         Adiciona um produto ao carrinho de compras.
        
        Verifica se o produto está na lista de produtos disponíveis antes de adicioná-lo ao carrinho.
        Se o produto já estiver no carrinho, sua quantidade será atualizada.
        '''
        item = None

        # Lê o arquivo de produtos disponíveis para verificar se o produto existe
        with open(caminho_lista_produtos, 'r', encoding='utf-8') as carrinho:
            leitor_csv = DictReader(carrinho, delimiter=',')
            for linha in leitor_csv:
                if linha['Nome'].lower() == nome.lower():
                    item = linha
                    break
        
        if not item:
            print("produto nao encontrado")

        else:
            carrinho_atualizado: list = []
            produto_encontrado: bool = False

            # Lê o carrinho atual para verificar se o produto já está nele
            with open(caminho_carrinho, 'r', encoding='utf-8') as carrinho:
                leitor_csv = DictReader(carrinho, delimiter=',')
                for linha in leitor_csv:
                    if linha['Nome'].lower() == nome.lower(): 

                        # Atualiza a quantidade do produto no carrinho
                        nova_quantidade: int = int(linha['quantidade']) + quantidade
                        linha['quantidade'] = str(nova_quantidade)
                        produto_encontrado = True
                    carrinho_atualizado.append(linha)

            # Se o produto não estiver no carrinho, adiciona um novo registro
            if not produto_encontrado:
                carrinho_atualizado.append({"Nome": item['Nome'], 'valor(R$)': item['valor(R$)'], 'quantidade': str(quantidade)})

            # Reescreve o arquivo do carrinho com a atualização
            with open(caminho_carrinho, 'w', newline='', encoding='utf-8') as carrinho:
                cabecalho = ['Nome', 'valor(R$)', 'quantidade']
                escritor_csv = DictWriter(carrinho, fieldnames=cabecalho)
                escritor_csv.writeheader()
                escritor_csv.writerows(carrinho_atualizado)

                if quantidade > 1:
                    print(f"{quantidade} {nome}s adicionados(as) ao seu carrinho")
                else:
                    print(f"um(a) {nome} adicionado(a) ao seu carrinho")


    def excluir_carrinho(self: object, nome: str) -> None:
        """
        Remove um produto do carrinho de compras, caso ele esteja presente.
        """

        produtos_restantes: list = []
        produto_encontrado: bool = False

        # Lê o carrinho e verifica se o produto está presente
        with open(caminho_carrinho, 'r', encoding='utf-8') as carrinho:
            leitor_csv = DictReader(carrinho, delimiter=',')
            for linha in leitor_csv:
                if linha['Nome'].lower() != nome.lower():
                    produtos_restantes.append(linha)
                else:
                    produto_encontrado = True
        
        # reescreve o carrinho sem o produto removido
        if produto_encontrado:
            with open(caminho_carrinho, 'w', newline='', encoding='utf-8') as carrinho:
                cabecalho = ['Nome', 'valor(R$)', 'quantidade']
                escritor_csv = DictWriter(carrinho, fieldnames=cabecalho)
                escritor_csv.writeheader()
                for produto in produtos_restantes:
                    escritor_csv.writerow(produto)
                print(f"{nome} excluido com sucesso!")
            
        else:
            print(f"{nome} nao encontrado")
    

    def visualizar_carrinho(self: object) -> None:
        with open(caminho_carrinho, 'r', encoding= 'utf-8') as carrinho:
            leitor_csv = DictReader(carrinho, delimiter = ',')
            produtos = list(leitor_csv)

            if not produtos:
                print("Nenhum item no carrinho")
            
            else:
                for linha in produtos:
                    print(f"{linha['Nome']} R${linha['valor(R$)']}, quantidade: {linha['quantidade']}")
    
    def comprar(self: object) -> float:
        """
        Calcula o valor total da compra somando os preços e quantidades dos produtos no carrinho.
        """

        valor_total: float = 0

        with open(caminho_carrinho, 'r', encoding='utf-8') as carrinho:
            leitor_csv = DictReader(carrinho, delimiter=',')
            for linha in leitor_csv:
                quantidade: int = int(linha['quantidade']) if linha['quantidade'] else 0
                preco: float = float(linha['valor(R$)']) if linha['valor(R$)'] else 0
                valor_total += quantidade * preco
            return valor_total
