import random

print("#-#" * 30)
print("Vamos jogar par ou impar?")
print("#-#" * 30)

cont = 0
valor = ''

while valor not in 'PI':
    numero = int(input("Digite um numero: "))
    valor = str(input("Par ou Impar?[P/I] ")).strip().upper()[0]
    numComp = random.randint(0, 10)
    total = numero + numComp
    print("Você jogou {} e o computador {}".format(numero,numComp),end=' ')
    if total % 2 == 0:
        print(", total deu {} par".format(total))
        if valor == "P":
            print("Você ganhou".format(total))
            cont += 1
            print("Vamos jogar novamente ")
        else:
            print("O computador ganhou".format(total))
            break
    else:
        print(", total deu {} impar".format(total))
        if valor == "I":
            print("Você ganhou".format(total))
            cont += 1
            print("Vamos jogar novamente ")
        else:
            print("O computador ganhou".format(total))
            break
print('-' * 50)
print('Game Over, Vc venceu {}'.format(cont))
