frase = input("Digite uma frase: ") # não foi usado a função strip, pois ela só retira os espaços do inicio e fim, e não de toda a string
fraseSemEspaco = frase.replace(" ","") #retira os todos os espaços da string
fraseAoContrario = "".join(reversed(fraseSemEspaco)) #função que inverte a palavra, chama o join para juntar todos os elementos da variavel, logo depois é chamado o reversed, onde inverte a palavra
if fraseSemEspaco == fraseAoContrario:
    print("Temos um palindromo")
else:
    print("Não temos um palindromo")

#Outra forma de fazer:

frase2 = input("Digite uma frase: ")
fraseSemEspaco2 = frase2.replace(" ","")
invertida = ""

for letra in frase2:
    invertida = letra + invertida #feito dessa forma a atribuição para conseguir inverter a string, se fosse feito dessa forma=invertida += letra, estaria atribuindo o valor de invertida + letra, onde não iria inverter a string
if fraseSemEspaco2 == invertida:
    print("Temos um PALINDROMO")
else:
    print("A palavra {} não é um palindromo".format(frase2))
