valorCasa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salário do comprador: "))
anos = int(input("Digite em quantos anos deve pagar: "))

parcela =  valorCasa / (anos * 12) #feito calculo para descrobir o valor da parcela mensal
porcentagem = salario * 30 / 100 # feito calculo para descobrir o valor da procentagem, seria 30 porcento de salario

print("Para pegar um empréstimo de R${:.2f} em {} anos a prestação será {:.2f} ao mês".format(valorCasa,anos,parcela))

if parcela <= porcentagem: #Feito if else para garantir que valide se a parcela é igual a 30 do salario
    print("Empréstimo CONCEDIDO")
else:
    print("Empréstimo NEGADO")