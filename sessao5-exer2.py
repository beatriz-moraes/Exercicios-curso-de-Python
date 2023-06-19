'''
SESSÃO 5 - Estruturas lógica e condicionais em python

2 - Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz
quadrada do número. Se for negativo, mostre uma mensagem dizend o queo número é inválido.
'''

import math

num = int(input("Digite um número: "))

if num % 2 == 0:
    raiz2 = math.sqrt(num)
    print(f"A raiz quadrada do número digitado é: {raiz2}")
else:
    print("Número digitado é invalido!")
