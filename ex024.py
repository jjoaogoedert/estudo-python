cidade = input("Digite o nome de uma cidade: ").strip() #função strip elimina os espaços

valida = cidade[:5]

print(valida.upper() == "SANTO")

#Outra forma de validar uma string, de dividir ela, tanto no começo quanto no fim
if cidade.upper().startswith('SANTO'):
    print(f"A cidade que vc digitou começa com santo, sua cidade {cidade}")
else:
    print(f"A cidade que vc digitou não começa com santo, sua cidade {cidade}")
