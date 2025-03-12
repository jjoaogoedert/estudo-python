nome = input("Digite seu nome completo: ")

print("O seu nome com todas as letras maisculas fica: ",nome.upper()) #mostra a string em letras maisculas
print("O seu nome com todas as letras minusculas fica: ",nome.lower()) #mostra a string em letras minusculas
print(f"O seu nome tem {len(nome) - nome.count(' ')} de letras ") #conta a quantidade de caracteres da string
primeiroNome = nome.split()[0] # pega somente a primeira parte da string, como seria um nome composto, joao henrique, iria dividir a string em posição1:joao e posição 2:henrique
print(f"O seu nome tem {len(primeiroNome)} de letras ") # aqui mostra a quantidade de caracteres da string
