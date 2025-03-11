string = input("Digite algo: ")
print("O tipo primitvo desse valor é: {}" , type(string)) #função type descobre o tipo da variavel
print("Só tem espaço? {}".format(string.isspace())) #Função isspace valida se a variavel é um espaço
print("É um número? {}".format(string.isnumeric())) #Função isnumeric, valida se a variavel é um numero
print("É alfabético? {}".format(string.isalpha())) #Função isalpha, valida se a variavel é alpha bético
print("É alfanumérico? {}".format(string.isalnum())) #Função isalnum, valida se a variavel é alpha numérico
print("Está em maiscula? {}".format(string.isupper())) #Função isupper, valida se a variavel é toda em letras maisculas
print("Está em minuscula? {}".format(string.islower())) # função islower, valida se a variavel é toda em letras minusculas
print("Está capitalizada? {}".format(string.istitle())) #funçao que valida a variavel se está capitalizada, se tem valor, e se não cai true nas funções de comparação com minuscula e maiscula