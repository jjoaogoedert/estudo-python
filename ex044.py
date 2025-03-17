print("=" * 10 + " LOJAS GOEDERT " + "=" * 10)
valor = int(input("Digite o valor da sua compra? "))
print("[ 1 ] à vista no dinheiro/débito")
print("[ 2 ] à vista no cartão")
print("[ 3 ] 2x no cartão")
print("[ 4 ] 3x ou mais no cartão")
opcao = int(input("Qual a opção? "))
if opcao == 1:
    desconto = (valor * 10) / 100
    total = valor - desconto
    print("Sua compra saiu por R${:.2f}, porem vai pagar R${:.2f}".format(valor,total))
elif opcao == 2:
    desconto = (valor * 5) / 100
    total = valor - desconto
    print("Sua compra saiu por R${:.2f}, porem vai pagar R${:.2f}".format(valor, total))
elif opcao == 3:
    print("Sua compra saiu por R${:.2f}".format(valor))
elif opcao == 4:
    parcelas = int(input("Digite a quantidade de parcelas: "))
    juros = valor + (valor * 20 / 100)
    print("As parcelas ficaram com o valor de R${:.2f} com {} parcelas".format(juros,parcelas))
    print("Sua compra saiu por R${:.2f}, porem vai pagar R${:.2f}".format(valor, juros))
else:
    print("Opção invalida, sua compra saiu por R${}".format(valor))