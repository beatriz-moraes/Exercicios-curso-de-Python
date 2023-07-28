'''
SESSÃO 5 - Estruturas lógica e condicionais em python

30 - Faça um programa que receba três números e mostre-os em ordem crescente.
'''

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))


variaveis = [num1, num2, num3]

variaveis_ordenadas = sorted(variaveis)

for variavel in variaveis_ordenadas:
    print(variavel)
