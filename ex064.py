numero = total = cont  = 0 #dessa forma definido todos os valores para as variaveis, onde todas recebem 0

while numero != 999: #enquanto numero for diferente de 999
    numero = int(input("Digite um numero[999 para parar]: "))
    total += numero
    cont += 1

print("Foi digitado {} numeros, a soma desses numeros digitados, fica: {}".format(cont - 1,total - 999)) #no format, cont -1, não considera a tentativa do numero 999, no total, ele subtrai o valor de 999