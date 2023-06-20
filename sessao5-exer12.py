'''
SESSÃO 5 - Estruturas lógica e condicionais em python

12 - Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número inválido".
Se o número for positivo, calcular o logaritmo deste número.
'''
import math

num = int(input("Digite um número inteiro: "))

if num < 0:
    print("Número inválido!")
else:
    log = math.log(num)
    print(f"O logaritmo no número é: {log}!")
