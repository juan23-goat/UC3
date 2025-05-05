def ler_usuario(nome_arquivo,):
    
    with open(nome_arquivo, 'r') as arquivo:
        return arquivo.read()

def escrever_Usuario(nome_arquivo, Usuarios):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(Usuarios)

escrever_Usuario('exemplo.txt', 'Joao, emailexemplo.com.br')
escrever_Usuario('exemplo.txt1', 'miguel, emailexemplo2.com.br')
print(ler_usuario('exemplo.txt'))
print(ler_usuario('exemplo.txt1'))

import os
if os.path.exists('exemplo.txt'):
    os.remove('exemplo.txt')
    print("Arquivo removido!")
else:
    print("Arquivo não encontrado.")
