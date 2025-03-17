numero = int(input("Digite um valor: "))
print("[ 1 ] converter para BINÁRIO")
print("[ 2 ] converter para OCTA")
print("[ 3 ] converter para HEXADECIMAL")
opcao = int(input("Digite qual a sua opção: "))

if opcao == 1:
    print("O valor do numero em binário {}".format(bin(numero)[2:])) #função bin, calcula o numero binário, e logo depois eu retirei os dois primeiros caracteres, para não aparecem com o [2:], ele coma a mostrar a variavel a partir do 2 caracter
elif opcao == 2:
    print("O valor do numero em octal  {}".format(oct(numero)[2:])) #função oct, calcula o octa do numero, logo depois coloquei o [2:], onde mostra após o segundo caracter
elif opcao == 3:
    print("O valor do numero em hexadecimal {}".format(hex(numero)[2:])) #funcao hex, calcula o hexadecimal do numero, logo depois coloquei o [2:] onde começa a mostrar a partir do segundo caracter
else:
    print("Opção inválida, tente novamente")