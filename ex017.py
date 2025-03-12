import math

catetoOposto = float(input("Digite um valor para o cateto oposto"))
catetoAdjacente = float(input("Digite um valor para o cateto adjacente"))

hipotenusa = math.sqrt((math.pow(catetoOposto,2))+(math.pow(catetoAdjacente,2))) #Função sqtr, faz o a raiz quadrada,  a função pow, faz a potencia de um valor, pelo espoente

print("O valor da hipotenusa é: {:.2f}".format(hipotenusa))

# Outras formas de fazerem

hipotenusaOutraForma = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)

print("O valor de hipotenusa é: {:.2f}".format(hipotenusaOutraForma))

# Outra forma de fazer

hipotenusaOutraForma2 = math.hypot(catetoOposto,catetoAdjacente) #Função hypot faz o calculo da hipotesuna, porem necessário passar os dois catetos

print("O valor de hipotenusa é: {:.2f}".format(hipotenusaOutraForma2))