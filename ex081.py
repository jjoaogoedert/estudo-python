lista = [] #Criado uma lista vazia
c = '' #Criado uma variavel que recebe string vazia
contador = 0 #Criado uma variavel que recebe vazio
contem = 'não faz' #Criado variavel para controle se o 5 faz ou não parte

while c != 'N':
    contador += 1
    numero = int(input("Digite um numero: "))
    lista.append(numero)
    if 5 in lista:
        contem = 'faz'
    c = str(input("Você quer continuar? S/N")).strip().upper()
print('-'*50)
print('Você digitou {} de elementos'.format(contador))
lista.sort(reverse=True)
print('A lista de forma decrescente fica {} '.format(lista))
print('O valor 5 {} parte da lista'.format(contem))

print("-" * 50)
print("Outra forma de fazer o código ")
print("-" * 50)

#De outra forma para mostrar se o 5 faz ou não parte
lista = [] #Criado uma lista vazia
c = '' #Criado uma variavel que recebe string vazia
contador = 0 #Criado uma variavel que recebe vazio
contem = 'não faz' #Criado variavel para controle se o 5 faz ou não parte

while c != 'N':
    contador += 1
    numero = int(input("Digite um numero: "))
    lista.append(numero)
    c = str(input("Você quer continuar? S/N")).strip().upper()

print('-'*50)
print('Você digitou {} de elementos'.format(contador))
lista.sort(reverse=True)
print('A lista de forma decrescente fica {} '.format(lista))
if 5 not in lista:
    print('O valor 5 não faz parte da lista')
else:
    print('O valor 5 faz parte da lista')