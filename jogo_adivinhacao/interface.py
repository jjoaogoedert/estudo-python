import time
import tkinter as tk
from tkinter import messagebox
from index import NumeroAleatorio
import pygame

#Instanciando as classes que serãp usadas
logica = NumeroAleatorio()
janela = tk.Tk()

#iniciando o modulo pygame para trabalhar com os sons do código
pygame.init()

#Criando a interface com o titulo e tamanho
janela.title("Jogo da adivinhação")
janela.geometry("500x500")

#função que valida o que é feito depois do clique
def clique():
    numero = entrada_num.get()
    result = logica.validaNumero(numero)
    if result:
        pass
    else:
        messagebox.showwarning('Alerta','Numero invalido, tente novamente')
        return

    retorno = logica.validaAcerto(numero)

    if retorno:
        pygame.mixer.music.load('sucesso.mp3')
        pygame.mixer.music.play()
        messagebox.showinfo('Sucesso', 'Parabéns você acertou')
        janela.withdraw()
    else:
        pygame.mixer.music.load('perdeu.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        messagebox.showinfo('Tente novamente',f'Parabéns você perdeu seu bananão, o numero era: {logica.numero_ale}')
        logica.gerarNovoNumero()

tk.Label(janela, text='Tente adivinhar o numero').pack(pady=5)
entrada_num = tk.Entry(janela)
entrada_num.pack(pady=5)

botao = tk.Button(janela,text='Tente Adivinhar',command=clique)
botao.pack(pady=20)

janela.mainloop()