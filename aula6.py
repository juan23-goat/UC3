#atv1

class Conta():

    def __init__(self, saldo, nome):
        self._saldo = saldo  
        self._nome = nome

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("Saldo invalido.")
        self._saldo = valor

    @property
    def nome(self):
        return self._nome.title()  

    @nome.setter
    def nome(self, valor):
        if len(valor) < 3:
            raise ValueError("Nome deve ter pelo menos 3 caracteres.")
        self._nome = valor

conta = Conta(20000, "juan")
conta.nome = "juan"
print(conta.nome)
conta.saldo = 20000
print(conta.saldo)



#atv2

