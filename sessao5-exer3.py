'''
SESSÃO 5 - Estruturas lógica e condicionais em python

3 - Leia um número real. Se o número for positivo imprima a raiz quadrada.
Do contrário, imprima o número ao quadrado.
'''

import math

num = float(input("Digite um número real: "))

if num % 2 == 0:
    raiz_quadrada = math.sqrt(num)
    print(f"A raiz quadrada do número digitado é: {raiz_quadrada}")
else:
    num_ao_quadrado = math.pow(int(num), 2)
    print(f"O número digitado ao quadrado é: {num_ao_quadrado}")
