lista = []

for i in range(5):
    numero = int(input(f"Digite um numero na posição {i} : "))
    lista.append(numero)

#Descrobrir os valores de maior e menor:
maior = max(lista)
menor = min(lista)

posicao_maior = [i for i,v in enumerate(lista) if v == maior]
posicao_menor = [i for i,v in enumerate(lista) if v == menor]

print('Vc digitou os valores {}'.format(lista))
print('O maior valor é {} e está na posicao {}'.format(maior,posicao_maior))
print('O menor valor é {} e está na posicao {}'.format(menor,posicao_menor))