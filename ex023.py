import math

numero = int(input("Digite um numero: "))

unidade = numero % 10 #É usado o operador módulo para descobrir o resto da divisão, que seria a unidade
dezena = (numero // 10) % 10 #É usado a divisão por inteiro para retirar a unidade, por exemplo, 1234, fica 123, assim depois é usado o resto da divisão para descobrir o ultimo digito
centena = (numero // 100) % 10 #É usado a divisão por inteiro por 100 para eliminar os dois primeiros digitos, por exemplo, 1234, fica 12, e logo depois é feito o resto da divisão para separar o utlimo numero
milhar = (numero // 1000) % 10 #É usado a divisão por inteiro por 1000 para eliminar os tres primeiros digitos, por exemplo, 1234, fica 1 somente, assim, já temos o valor de milhar, e dividimos para saber qual o valor, 1 % 10 = 1

print(f"A unidade {unidade}")
print(f"A dezena {dezena}")
print(f"A centena {centena}")
print(f"A milhar {milhar}")