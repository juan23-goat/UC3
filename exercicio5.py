#Cada numeração corresponde a um programa diferente para que seja desenvolvido. As atividades seguem abaixo:

#1.Filtre produtos com preço > 1000 usando list comprehension;

#2.Conte quantos produtos existem por categoria (usar dicionário);

#3.Remova duplicatas de uma lista de pedidos usando set.

#4.Uma empresa contratou seus serviços para armazenar dados de colaboradores em memória e realizar operações como:
'''
Adicionar novos colaboradores.
Buscar colaborador por ID.
Listar colaboradores com salário acima de X.
'''
#Implemente utilizando funções.


#1
produtos = [
    {"nome": "Notebook", "preco": 2500},
    {"nome": "Mouse", "preco": 150},
    {"nome": "Monitor", "preco": 1200},
    {"nome": "Teclado", "preco": 300}
]

produtos_caros = [produto for produto in produtos if produto["preco"] > 1000]

print(produtos_caros)


#2
# Lista de produtos com suas categorias
produtos = [
    {"nome": "Notebook", "categoria": "Eletrônicos"},
    {"nome": "Mouse", "categoria": "Eletrônicos"},
    {"nome": "Camiseta", "categoria": "Roupas"},
    {"nome": "Calça", "categoria": "Roupas"},
    {"nome": "Geladeira", "categoria": "Eletrodomésticos"},
    {"nome": "Fogão", "categoria": "Eletrodomésticos"},
    {"nome": "Micro-ondas", "categoria": "Eletrodomésticos"}
]

def contar_por_categoria(produtos):
    contagem = {}
    for produto in produtos:
        categoria = produto["categoria"]
        if categoria in contagem:
            contagem[categoria] += 1
        else:
            contagem[categoria] = 1
    return contagem


resultado = contar_por_categoria(produtos)
print(resultado)







#3
lista = {1, 2, 3,3, 4, 4}
print(lista)



#4 

colaboradores = []


def adicionar_colaborador(nome, id, salario):
    colaborador = {
        "nome": nome,
        "id": id,
        "salario": salario
    }
    colaboradores.append(colaborador)
    print(f"Colaborador {nome} adicionado com sucesso.")


def buscar_por_id(id):
    for c in colaboradores:
        if c["id"] == id:
            return c
    return "Colaborador não encontrado."


def listar_salario_acima(valor):
    return [c for c in colaboradores if c["salario"] > valor]



adicionar_colaborador("João", 100, 1000)
adicionar_colaborador("Ana", 101, 500)
adicionar_colaborador("Matheus", 102, 2000)


print(buscar_por_id(100))  

print(listar_salario_acima(1000))  