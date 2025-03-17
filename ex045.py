import random
from time import sleep

print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
try:
    opcao = int(input("Qual a sua jogada? "))
    if opcao not in [1,2,3]:
        raise ValueError("Opção inválida! Escolha entre 0, 1 ou 2.")

    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO")

    itens = ('Pedra','papel','Tesoura')
    aleatorio = random.randint(0,2)

    print("-=-" * 10)
    print(f"Computador jogou: {itens[aleatorio]}")
    print(f"Jogador jogou: {itens[opcao]}")
    print("-=-" * 10)

    if opcao == 0:
        if aleatorio == 1:
            print("Jogador venceu!!!")
        elif aleatorio == 0:
            print("Jogo empatou!!!")
        elif aleatorio == 2:
            print("Computador venceu!!!")
    elif opcao == 1:
        if aleatorio == 0:
            print("Jogador venceu!!!")
        elif aleatorio == 1:
            print("Jogo empatou!!!")
        elif aleatorio == 2:
            print("Computador venceu!!!")
    elif opcao == 2:
        if aleatorio == 0:
            print("Computador venceu!!!")
        elif aleatorio == 1:
            print("Jogador venceu!!!")
        elif aleatorio == 2:
            print("Jogo empatou!!!")
except ValueError as e:
    raise ValueError("Opção inválida! Escolha entre 0, 1 ou 2.")
