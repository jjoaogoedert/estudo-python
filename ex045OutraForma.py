import random

print('''[0] PEDRA
[1] PAPEL
[2] TESOURA
''')

itens = ('Pedra','Papel','Tesoura')
try:
    opcao = int(input("Sua vez de jogar: "))
    if opcao not in [0,1,2]:
        raise ValueError("Opção invalida, tente novamente")
    print("")
    aleatorio = random.randint(0,2)
    if (opcao == 0 and aleatorio == 2) or (opcao == 1 and aleatorio == 0) or (opcao == 2 and aleatorio == 1):
        print("O jogador venceu")
    else:
        print("O computador perdeu")
except ValueError as e:
    print("Erro:", e)