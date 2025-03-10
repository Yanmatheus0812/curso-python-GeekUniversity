from random import randint, choice

class Calcular:

    __simbolos: list = ["+", "-", "*"]

    def __init__(self: object, dificuldade: int) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1 : int = self.gerar_valor()
        self.__valor2: int = self.gerar_valor()
        self.__operacao: int = choice(self.__simbolos) 
        self.__resultado: int = self.gerar_resultado()
    
    @property
    def simbolos(self: object) -> list:
        return self.__simbolos

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1
    
    @property
    def valor2(self: object) -> int:
        return self.__valor2
    
    @property
    def operacao(self: object) -> int:
        return self.__operacao
    
    @property
    def resultado(self: object) -> int:
        return self.__resultado
    
    def gerar_valor(self: object) -> int:
        if self.__dificuldade == 1:
            return randint(1, 5)
        
        elif self.__dificuldade == 2:
            return randint(6, 10)
        
        elif self.__dificuldade == 3:
            return randint(11, 15)
    
    def gerar_resultado(self: object) -> int:
        if self.__operacao == "+":
            return self.__valor1 + self.__valor2
        
        elif self.__operacao == "-":
            return self.__valor1 - self.__valor2
        
        elif self.__operacao == "*":
            return self.__valor1 * self.__valor2
