lista = list()
expressao = ''

expressao = str(input('Digite a expressão numérica: '))
for v in expressao:
    if v == '(':
        lista.append(v)
    elif v == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append('erro')
            break

if len(lista) == 0:
    print('A expressão está correta')
else:
    print('A expressão está incorreta')