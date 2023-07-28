'''
SESSÃO 5 - Estruturas lógica e condicionais em python

33 - Um produto vai sofrer aumento de acordo com a tabela abaixo.
Leia o preço antigo, calcule e escreva o preço novo, e escreva uma mensagem
em função do preço novo (de acordo com a segunda tabela)

       PREÇO ANTIGO           PERCENTUAL DE AUMENTO        PREÇO NOVO                              MENSAGEM
       Até R$50,00                     5%                  Até R$80,00                              Barato
       Entre R$50 e R$100              10%                 Entre R$80,00 e R$120,00(inclusive)      Normal
       Acima de R$100,00               15%                 Entre R$120,OO e R$200(inclusive)        Caro
                                                           Acima de R$200                           Muito Caro
'''
produto = input("Qual o nome do produto? ")
preco = float(input("Digite o preço do produto atual: "))

if preco < 50:
    aumento = preco * 5 / 100 + preco
    print(f"O produto {produto} tinha o valor R${preco}, aumentou 5% e passou a ser: R${aumento}!")
elif preco > 100:
    aumento = preco * 15 / 100 + preco
    print(f"O produto {produto} tinha o valor R${preco}, aumentou 15% e passou a ser: R${aumento}!")
else:
    aumento = preco * 10 / 100 + preco
    print(f"O produto {produto} tinha o valor R${preco}, aumentou 10% e passou a ser: R${aumento}!")

if aumento < 80:
    print("Barato!")
elif aumento <= 120:
    print("Normal!")
elif aumento <= 200:
    print("Caro!")
else:
    print("Muito caro!")