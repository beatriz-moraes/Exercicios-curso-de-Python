'''
SESSÃO 5 - Estruturas lógica e condicionais em python

6 - Faça um programa que, dados dois números inteiros, mostre na tela
o maior deles, assim como a diferença entre ambos.
'''

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

if num1 > num2:
    print(f"O número {num1} é maior do que o número {num2}!")
    print(f"Com a diferença de {num1 - num2} número(s) entre eles!")
else:
    print(f"O número {num2} é maior do que o número {num1}!")
    print(f"Com a diferença de {num2 - num1} número(s) entre eles!")
