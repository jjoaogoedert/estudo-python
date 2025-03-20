print("=" * 30)
print("10 termos de um PA")
print("=" * 30)

primeiroTermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
contador = 1
termo = primeiroTermo
total = 0
mais = 10
while mais != 0: #while usado para validar se a variavel mais é diferente de 0, se for continua o código
    total = total + mais #atribui o valor de total + mais , em total
    while contador <= total: #realizei um while, onde ele vai mostrar os termos do numero a partir da validação da variavel total, onde a variavel total soma sempre 1 quando entra nesse while
        print("{} -> ".format(termo), end=' ')
        termo += razao
        contador += 1
    print("Pausa")
    mais = int(input("\nQuantos termos vc quer ver? "))
print("Acabou")
