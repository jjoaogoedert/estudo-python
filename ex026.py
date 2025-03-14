frase = input('Digite uma frase: ').upper().strip() #Função strip elimina os espaços
letra = 'A'
quantidade = frase.count(letra) #função counta realiza uma contagem, assim, estamos contando quantas letras a possuem na string
primeiraLetra = frase.find(letra) #função find, procura a primeira letra na string, onde estamos procurando a letra a
ultimaLetra = frase.rfind(letra) #função rfind, procura a ultima letra na string, onde estamos procurando a letra a
print(f"A quantidade de vezes que apresentou a letra a é {quantidade}, a primeira letra está na posição {primeiraLetra},"
      f" a ultima letra está na posição {ultimaLetra}")


# Outra forma de fazer, sendo mais eficiente e prática, porem mais dificil de ler
print("A quantidade de letras {}".format(frase.count('A')))
print("A primeira letra A da palavra se encontra na posição {}".format(frase.find('A')))
print("A ultima letra A da palavra se encontra na posição {}".format(frase.rfind('A')))