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


#atv2/4




class AnimalMeta(type):
    def __new__(cls, name, bases, dct):
       
        if 'fazer_som' not in dct:
            raise TypeError(f"A classe {name} deve ter o método 'fazer_som'!")
        return super().__new__(cls, name, bases, dct)

class Animal(metaclass=AnimalMeta):
    def __init__(self, nome):
        self.nome = nome

class Gato(Animal):
    def __init__(self, nome, miar, comer, beber):
        super().__init__(nome)  
        self.miar = miar
        self.comer = comer
        self.beber = beber

    def fazer_som(self):
        print(f"{self.nome} faz: {self.miar}")
        
    def alimentar(self):
        print(f"{self.nome} está comendo {self.comer}.")
        
    def beber_agua(self):
        print(f"{self.nome} está bebendo {self.beber}.")

class Cachorro(Animal):
    def __init__(self, nome, latir, comer, beber):
        super().__init__(nome) 
        self.latir = latir
        self.comer = comer
        self.beber = beber

    def fazer_som(self):
        print(f"{self.nome} faz: {self.latir}")
        
    def alimentar(self):
        print(f"{self.nome} está comendo {self.comer}.")
        
    def beber_agua(self):
        print(f"{self.nome} está bebendo {self.beber}.")

gato = Gato("Pudim", "Miau", "ração", "água")
cachorro = Cachorro("Rex", "AuAu", "ração", "água")

gato.fazer_som()
gato.alimentar()
gato.beber_agua()

print()

cachorro.fazer_som()
cachorro.alimentar()
cachorro.beber_agua()

#atv3/4


class RepositorioMeta(type):
    def __new__(cls, name, bases, dct):
        if 'cadastrar' not in dct:
            raise TypeError(f"A classe {name} deve ter o método 'cadastrar'!")
        return super().__new__(cls, name, bases, dct)

class UsuarioRepository(metaclass=RepositorioMeta):
    def __init__(self):
        self.usuarios = {}

    def cadastrar(self, usuario):
        if usuario['email'] not in self.usuarios:
            self.usuarios[usuario['email']] = usuario
            print("Usuário cadastrado com sucesso!")
        else:
            print("Email já cadastrado!")

    def listar_todos(self):
        return list(self.usuarios.values())

    def buscar_por_email(self, email):
        return self.usuarios.get(email, None)

    def remover(self, email):
        if email in self.usuarios:
            del self.usuarios[email]
            print("Usuário removido com sucesso!")

    def atualizar(self, usuario):
        if usuario['email'] in self.usuarios:
            self.usuarios[usuario['email']] = usuario
            print("Usuário atualizado com sucesso!")
        else:
            print("Usuário não encontrado!")

    def listar_por_nome(self, nome):
        return [user for user in self.usuarios.values() if user['nome'] == nome]

    def listar_por_email(self, email):
        return [user for user in self.usuarios.values() if user['email'] == email]

    def listar_por_nome_e_email(self, nome, email):
        return [user for user in self.usuarios.values() if user['nome'] == nome and user['email'] == email]

repo = UsuarioRepository()

repo.cadastrar({"nome": "Alice", "email": "alice@example.com"})
repo.cadastrar({"nome": "Joao", "email": "joao@example.com"})
repo.cadastrar({"nome": "Alice", "email": "alice123@example.com"})

print(repo.listar_todos())

print(repo.buscar_por_email("alice@example.com"))

repo.atualizar({"nome": "Alice", "email": "alice@example.com"})

repo.remover("joao@example.com")

print(repo.listar_por_nome("Alice"))

print(repo.listar_por_nome_e_email("Alice", "alice123@example.com"))

