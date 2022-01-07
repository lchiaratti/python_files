

class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print("Contruindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print("Saldo é de {} do titular {}".format(self.__saldo, self.__titular))

    def deposito(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saque(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou do limite".format(valor))

    def transfere(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)
    
    @property
    def saldo(self):
        return self.__saldo
     
    @property
    def titular(self):
        return self.__titular        

    @property
    def limite(self):
        return self.__limite
  
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
