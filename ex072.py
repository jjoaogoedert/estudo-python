numeros = (
    'Zero',
    'Um',
    'Dois',
    'Três',
    'Quatro',
    'Cinco',
    'Seis',
    'Sete',
    'Oito',
    'Nove',
    'Dez',
    'Onze',
    'Doze',
    'Treze',
    'Quatorze',
    'Quinze',
    'Desseseis',
    'Dessesete',
    'Dezoito',
    'Dezenove',
    'Vinte'
)
while True:
    num = int(input("Digite um valor entre 0 e 20: "))
    if 0 <= num <= 20:
        break
print("Valor que vc digiou é {}".format(numeros[num]))