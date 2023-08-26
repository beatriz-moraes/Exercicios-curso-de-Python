'''
SESSÃO 5 - Estruturas lógica e condicionais em python

35 - Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12,
e se o dia existe naquele mês. Note que fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não bissextos.

'''

from calendar import isleap

dia = int(input("Digite o dia desejado: "))
mes = int(input("Digite o mês desejado: "))
ano = int(input("Digite o ano desejado: "))
bissexto = False

if isleap(ano):
    bissexto = True

if mes <1 and mes >12:
    print("Mês inválido!")
    exit()
if dia < 1:
    print("Mês inválido!")
    exit()
if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10) and (dia > 31):
    print("Mês inválido!")
    exit()
elif (mes == 2) and ((not bissexto and dia >28) or (bissexto and dia > 29)):
    print("Mês inválido!")
    exit()
elif dia > 30:
    print("Mês inválido!")
    exit()
else :
    print("Data válida!")
    