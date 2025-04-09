produtos = {
    'sabao': 12.10,
    'detergente': 2.90,
    'pão': 1.10,
    'manteiga': 3.40,
    'chocolate': 4.90,
    'queijo': 11.50,
    'bacon': 12.20,
    'carne': 9.80,
    'macarrão': 6.10,
    'refigerante': 8.05,
    'agua': 1.70,
    'saco de lixo': 2.80
}

print("-" * 50)
print(f'{"Listagem de compras":^50}') #Essa concatenação serve para alinhar o texto, deixamos ele no centro da linha
print("-" * 50)
for nome,preco in produtos.items():
    pontos = '.' * (50 - len(nome) - len(f"R${preco:.2f}") - 1) #Fiz esse calculo para a quantidade de pontos ficar dinamica
    print('{} {} R${:.2f}'.format(nome,pontos,preco))
print("-" * 50)