largura = float(input("Digite a largura da parede para calcularmos a quantidade de tinta: "))
altura = float(input("Digite a altura da parede para calcularmos a quantidade de tinta: "))
area = largura * altura
print("A sua parede tem a dimensão de {}x{} e sua area é de {}m²".format(largura,altura,area))
tinta = area / 2
print("A quantidade de tinta para pintar a sua parede, de {:.2f} de largura e {:.2f} de altura, é: {:.2f} litros".format(largura,altura,tinta))