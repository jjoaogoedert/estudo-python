nomeCompleto = input("Digite seu nome completo: ").strip() #retira os espaços da variavel de string
partes = nomeCompleto.split() #divide a variavel a partir do espaço em branco, ex josué alberto, [0]=josué, [1]alberto
print("Muito prazer em te conhecer!")
print(f"Seu primeiro nome é {partes[0]}")
print("Seu segundo nome é {}".format(partes[len(partes)-1])) #Aqui a função len, le o tamanho da string, quantos caracteres tem,