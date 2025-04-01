brasileirao = (
    'Botafogo',
    'Palmeiras',
    'Flamengo',
    'Fortaleza',
    'Internacional',
    'São Paulo',
    'Corinthians',
    'Bahia',
    'Cruzeiro',
    'Vasco da Gama',
    'Vitória',
    'Atlético-MG',
    'Fluminense',
    'Gremio',
    'Juventude',
    'Bragantino',
    'Athletico-Pr',
    'Criciuma',
    'Atlético-go',
    'Cuiaba'
)

print("Os primeiros 5 colocados do brasileirão 2024 foram: {}".format(brasileirao[:6]))
print("Os ultimos 4 colocados do brasileirao foram: {}".format(brasileirao[5:]))
print("Os ultimos 4 colocados do brasileirao foram: {}".format(sorted(brasileirao))) #função sorted funciona para ajustar um arary, ordenar ele, pelo alfabaeto, se quiser ordenar de tras para frente, passar o terceiro parametro como True
for i in range(len(brasileirao) - 1): #aqui ele vai percorrendo cada posição do array
    if brasileirao[i] == 'Botafogo':
        print('Botafogo está na posição {}'.format(i + 1))
#pode ser feito de outra forma essa busca de valor, seguinte forma:
print("O botafogo está na posição: {}".format(brasileirao.index('Botafogo') + 1))