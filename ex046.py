from time import sleep #import do modulo de time->sleep, onde serve para deixar o código esperando, literalmente dormindo
import pygame #import do modulo pygame, para jogos, porem serve para trabalhar com musica, onde estou manipulando um valor de musica, mp3

for a in range(10,-1,-1): #For, é passado a variavel de controle, Variavel a, depois passado a função range, onde manipula um intervalo, da forma que está manipula de 10 até -1, o primeiro parametro é onde começa o intervalo, o segundo é aonde termina o intervalo, e o terceiro é quantidade de vezes que é percorrido, por exemplo, hoje está -1, onde iria percorrer de 10->9->8->7....
    sleep(0.5)
    print(a)

pygame.init() #inicia o init do modulo
pygame.mixer.music.load("somFoguete.mp3") #faz o load da musica, do arquvio mp3, que procura no projeto
pygame.mixer.music.play() #da o play no arquivo mp3
sleep(6) #faz com que o código espere 6 segundos
print("BUMMMMMMMMMMMMMMMMMMM! POWWWWWWWWWWWW 🎆🎆🎆")
pygame.mixer.music.stop() #da um stop na musica