from calcular import Calcular

pontos: int = 0

print("Bem-vindo ao jogo da matematica! Selecione a dificuldade para iniciar")
print("1- Facil")
print("2- Medio")
print("3- Dificil")
escolha: int = int(input("Escolha a dificuldade: "))

if escolha < 1 or escolha > 3:
    print("Dificuldade nao existe, tente novamente...")
    exit()

while True:
    Jogo = Calcular(escolha)

    print(f"{Jogo.valor1} {Jogo.operacao} {Jogo.valor2}")

    resultadoParcial: int = int(input("Sua resposta: "))

    if resultadoParcial == Jogo.resultado:
        pontos += 1
        print(f"Acertou! Sua pontuacao atual e: {pontos} pontos!")
    
    else:
        print(f"Que pena... o resultado era {Jogo.resultado}, sua pontuacao total foi de {pontos} pontos!")
        exit()
