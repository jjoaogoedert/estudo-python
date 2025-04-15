palavras = (
    'Estudar',
    'Melhor',
    'Forma',
    'De',
    'Se',
    'Destacar',
    'E',
    'Conseguir',
    'Enteder',
    'Que',
    'Tudo',
    'Que',
    'Voce',
    'Aplica',
    'Qualquer',
    'Mero',
    'Esforço',
    'Ira',
    'Ter',
    'Conhecimento'
)
vogais = ('A','E','I','O','U')

for palavra in palavras:
    vogais_mostradas = []
    print("A palavra {} tem de vogais: ".format(palavra),end=" ")
    for letra in palavra:
        if letra.upper() in vogais and letra not in vogais_mostradas:
            print(letra,end=" ")
            vogais_mostradas.append(letra)
    print()