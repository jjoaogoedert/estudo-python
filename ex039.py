from datetime import date #importado modulo de data, para descrobir o ano atual
ano = int(input("Digite o ano de nascimento: "))
dataAtual = date.today().year #chamado função de date para descobrir a data atual, seria today.year, busca somente o ano
idade = dataAtual - ano
print("Quem nasceu em {}, tem em {} {} anos".format(ano,dataAtual,idade))

if idade < 18:
    anosFaltando = 18 - idade
    print("Você não precisa se alistar agora, mas vai ter que se alistar da qui a {} anos".format(anosFaltando))
elif idade == 18:
    print("Você precisa se alistar IMEDIATAMENTE")
else:
    anosPassou = idade - 18
    print("Você não precisa se alistar mais, seu alistamento foi ah {} anos".format(anosPassou))