import random

numeroAle = random.randint(0,10) #função randint, gera um numero aleatório com um intervalo especifico
print("Sou seu computador, pensei em um numero de 0 a 10")
print("Será que vc terá capacidade para acertar?")
contador = 1
acertou = False

while not acertou:
    tentativa = int(input("Qual o seu palpite? "))
    if tentativa == numeroAle:
        acertou = True
    else:
        contador += 1
        if tentativa > numeroAle:
            print("Menos... Tente outra vez")
        else:
            print("Mais... Tente outra vez")

print("⭐ !!!Você acertou!!!  ⭐")
print("Precisou de {} tentativas".format(contador))

###outra forma de fazer, que achei mais facil de compreender

numeroAle = random.randint(0,20) #função randint, gera um numero aleatório com um intervalo especifico
print("Sou seu computador, pensei em um numero de 0 a 20")
print("Será que vc terá capacidade para acertar denovo?")
tentativa = int(input("Qual o seu palpite? "))
contador = 1

while tentativa != numeroAle:
    contador += 1
    if tentativa > numeroAle:
        print("Menos... Tente outra vez")
    else:
        print("Mais... Tente outra vez")
    tentativa = int(input("Qual o seu palpite? "))

print("⭐ !!!Você acertou!!!  ⭐")
print("Precisou de {} tentativas".format(contador))