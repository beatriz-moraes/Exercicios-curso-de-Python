'''
SESSÃO 5 - Estruturas lógica e condicionais em python

7 - Faça um programa que receba dois números e mostre o maior.
Se por acaso,os dois números forem iguais, imprima a mensagem números iguais.
'''

num1 = (input("Digite o primeiro número:"))
num2 = (input("Digite o segundo número:"))

if num1 > num2:
    print(f"O número {num1} é maior do que o número {num2}!")
elif num2 == num1:
    print("Os números digitados são iguais!")
else:
    print(f"O número {num2} é maior do que o número {num1}!")
