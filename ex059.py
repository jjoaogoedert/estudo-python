from time import sleep

soma = 0
multiplica = 0
maior = 0

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opcao = 0
while opcao != 5:
    print("-=" * 20)
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos numeros
    [ 5 ] Sair do programa ''')
    opcao = int(input(">>>>>>> Qual a sua opção? "))
    if opcao == 1:
        soma = n1 + n2
        print("A soma dos numeros ficou: {}".format(soma))
    elif opcao == 2:
        multiplica = n1 * n2
        print("A multiplicação dos numeros ficou: {}".format(multiplica))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("O maior valor dos numeros é {}".format(maior))
    elif opcao == 4:
        print("Informe os numeros novamente: ")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Finalizando.....")
        sleep(1)
    else:
        print("Opção invalida tente novamente")
print("Fim do programa!")
