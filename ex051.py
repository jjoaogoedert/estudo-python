print("=" * 30)
print("10 termos de um PA")
print("=" * 30)

primeiroTermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
decimo = primeiroTermo + (10 - 1) * razao #calculo que calcula o termo pa do numero

for i in range(primeiroTermo,decimo,razao):
    print("{}".format(i), end=' -> ')
print("ACABOU")