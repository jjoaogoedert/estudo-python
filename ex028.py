import random

numeroAle = random.randint(0,5) #função randint, gera um numero aleatório com um intervalo especifico
tentativa = int(input("Tente adivinhar o numero secreto: "))

print("-=-" * 20) #aqui está multiplicando a string 20 vezes, ficou assim: -=--=--=--=--=-...... continua até 20
if tentativa == numeroAle:
    print("⭐ !!!Você acertou!!!  ⭐")
else:
    print(f"Você perdeu, o numero era {numeroAle}! 😔")
print("-=-" * 20)