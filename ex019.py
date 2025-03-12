import random

nomes = []

for i in range(4):
    nome = input(f"Digite um aluno {i+1} ")
    nomes.append(nome)

sorteio = random.choice(nomes) #rando.choice faz a escolhe de um elemento em um array, geralmente usado para fazer um programa de sorteio

print("O nome escolhido é:",sorteio)


# outra forma de fazer

n1 = input("Digite o primeiro nome: ")
n2 = input("Digite o segundo nome: ")
n3 = input("Digite o terceiro nome: ")
n4 = input("Digite o quarto nome: ")
lista = [n1,n2,n3,n4]
escolha = random.choice(lista)
print("O nome escolhido foi: ",escolha)