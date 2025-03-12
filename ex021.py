import pygame #modulo para criação de jogos, onde tem musicas

pygame.init() #iniciamos o módulo/biblioteca
pygame.mixer.music.load("som.mp3") #adicionamos a url da musica, para rodar a msuica
pygame.mixer.music.play() #aqui damos play na musica

input("Digite enter para parar") #quando o usuario apertar enter para a aplicação
pygame.mixer.music.stop() #aqui para o envento de musica com stop
