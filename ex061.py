print("=" * 30)
print("10 termos de um PA")
print("=" * 30)

primeiroTermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
decimo = primeiroTermo + (10 - 1) * razao #calculo que calcula o termo pa do numero
contador = 1
total = primeiroTermo

while contador <=10: #realizei um while, onde ele vai fazer 10 vezes o pa de um numero
    contador += 1
    print("{}".format(total), end=' -> ')
    total += razao
print("ACABOU")