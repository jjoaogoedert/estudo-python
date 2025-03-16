velocidade = int(input("Digite a valocidade que vc estava: "))

if velocidade > 80:
    print("Você foi multado por excesso de velocidade")
    total = velocidade - 80
    multa = total * 7
    print("O valor da multa que vc precisa pagar é: R${:.2f}".format(multa))
else:
    print("Você está seguindo as regras corretamente, obrigado por ajudar a sociedade")