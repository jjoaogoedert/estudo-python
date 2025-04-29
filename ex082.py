lista = list()
pares = list()
impares = list() #Definido dessa forma as listas, pois fazendo tudo em uma mesma linha ele informa que todas as listas seguem o mesmo array, então iriam todas ter o mesmo valor
c = ''

while c != 'N':
    numero = int(input("Digite um valor: "))
    lista.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    c = str(input('Você quer continuar? S/N ')).strip().upper()
print('Os numeros digitados foram {}'.format(lista))
print('Os numeros pares digitados foram {}'.format(pares))
print('Os numeros impares digitados foram {}'.format(impares))

#Outra forma de implementar, mais dinamico, porem usa duas estruturas de repetirção, onde deve dificultar o entendimento do código
print("-" * 60)
print('Outra forma de implementar')
lista.clear()
pares.clear()
impares.clear()
while True:
    lista.append(int(input('Digite um numero')))
    c = str(input("Vc quer continuar? S/N "))
    if c in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-'*55)
print(f'Os numeros digitados foram {lista}')
print(f'Os numeros pares digitados foram {pares}')
print(f'Os numeros impares digitados foram {impares}')