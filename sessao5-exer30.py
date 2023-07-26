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

'''
if num1 > num2 and num1 > num3 and num2 > 3:
    maior = num1
    seg_maior = num2
elif num2 > num1 and num2 > num3 and num1 > num3:
    maior = num2
    seg_maior = num1
elif num3 > num1 and num3 > num2  and num1 > num2:
    maior = num3
    seg_maior = num1
'''