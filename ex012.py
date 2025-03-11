precoProduto = int(input("Digite o valor de um produto em R$: "))
desconto = (precoProduto * 5) / 100
total = precoProduto - desconto
print("O valor de seu produto {}, com o desconto de 5% fica: {}".format(precoProduto,total))