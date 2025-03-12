import math

angulo = float(input("Digite um valor para o angulo"))

angulo_radians = math.radians(angulo)

seno = math.sin(angulo_radians) #função sin retorna o seno do angulo
cosseno = math.cos(angulo_radians) #função cos retorna o cosseno do angulo
tangente = math.tan(angulo_radians) #função tan retorna a tangente do angulo

print("O angulo tem o seno de {:.2f}, o cosseno {:.2f}, a tangente {:.2f}".format(seno,cosseno,tangente))