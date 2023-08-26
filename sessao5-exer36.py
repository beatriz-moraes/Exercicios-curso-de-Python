'''
SESSÃO 5 - Estruturas lógica e condicionais em python

36 - Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser
paga ao vendedor. Para calcular a comissão, considere a tabela abaixo:

Venda mensal                                                  Comissão
Maior ou igual a R$100.000,00                               R$700,00 + 16% das vendas
Menor que R$100.000,00 e maior ou igual a R$80.000,00       R$650,00 + 14% das vendas
Menor que R$80.000,00 e maior ou igual a R$60.000,00        R$600,00 + 14% das vendas
Menor que R$60.000,00 e maior ou igual a R$40.000,00        R$550,00 + 14% das vendas
Menor que R$40.000,00 e maior ou igual a R$20.000,00        R$500,00 + 14% das vendas
Menor que R$20.000,00                                       R$400,00 + 14% das vendas

'''

valor_venda = float(input("Qual o valor de venda mensal feita pelo vendedor: "))

if valor_venda >= 100000:
    comissao = 700 + valor_venda * 16 / 100
    print(f"O vendedor fez a venda maior de R$100.000,00 e irá receber a comissão de: R$ {comissao:,.2f}")
elif valor_venda >= 80000:
    comissao = 650 + valor_venda * 14 / 100
    print(f"O venedor fez a venda entre R$100.000,00 a 80.000,00 e irá receber a comissão de: R$ {comissao:,.2f}")
elif valor_venda >= 60000:
    comissao = 600 + valor_venda * 14 / 100
    print(f"O vendedor fez a venda entre R$80.000,00 a R$60.000,00 e irá receber a comissão de: R$ {comissao:,.2f}")
elif valor_venda >= 40000:
    comissao = 550 + valor_venda * 14 / 100
    print(f"O vendedor fez a venda entre R$60.000,00 a R$40.000,00 e irá receber a comissão de: R$ {comissao:,.2f}")
elif valor_venda >= 20000:
    comissao = 500 + valor_venda * 14 / 100
    print(f"O vendedor fez a venda entre R$40.000,00 a R$20.000,00 e irá receber a comissão de: R$ {comissao:,.2f}")
else:
    comissao = 400 + valor_venda * 14 / 100
    print(f"O vendedor fez a venda menor que R$20.000,00 e irá receber a comissão de: R$ {comissao:,.2f}")

