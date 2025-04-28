lista = [] #Definido um array
c = '' #Definido um variavel de controle

while c != 'N': #estrutura de controle para fazer a validação se o usuario quer continuar ou não
    numero = int(input('Digite um valor: ')) #Definido uma variavel para receber o valor que o usuario vai digitar
    if numero not in lista: #validação se na lista [], contem o numero que o usuario digitou
        lista.append(numero) #adiciona o numero no final da lista
        print("Valor adicionado com sucesso...") #Mensagem em tela
    else:
        print("Valor duplicado, não vou inserir ele") #mensagem em tela

    c = str(input('Vc quer continuar? S/N: ' )).strip().upper() #Pergunta ao usuario se quer continuar

lista.sort() #Metodo está fazendo com que o array fique ordenado, onde
print('-=' * 55)
print(f"Lista com os numeros ficou {lista}")
