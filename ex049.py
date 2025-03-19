total = 0
controle = 0
numero = int(input("Digite um numero para saber sua tabuada: "))

for i in range(1,11): #feito for com 2 parametros na funcao range, pois é padrao sempre adicionar 1 na varaivel de controle
    total = numero * i
    print("{} X {} = {}".format(numero,i,total))