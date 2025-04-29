lista = []
i = 0

for i in range(0,5):
    numero = int(input("Digite um numero"))
    if lista == []:
        lista.append(numero)
        print('Numero adicionado ao final da lista')
    elif numero > lista[i]:
        print('Numero adicionado ao final da lista')
    elif numero < lista[i]:
        print('Numero adicionado a posição zero da lista')
