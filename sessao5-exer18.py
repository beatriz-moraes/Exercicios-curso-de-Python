'''
SESSÃO 5 - Estruturas lógica e condicionais em python

18 - Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas (as básicas, por exemplo).
O usuário escolhe uma das opções e o seu programa então pede dois valores numéricos e realiza a operação, mostrando
o resultado e saindo.
'''

operacao = int(input("Qual operação deseja realizar: 1- soma, 2- subtração, 3- multiplicação ou 4- divisão: "))
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if operacao == 1:
    soma = num1 + num2
    print(f"A soma de {num1} + {num2} = {soma}")
elif operacao == 2:
    subtracao = num1 - num2
    print(f"A subtração de {num1} - {num2} = {subtracao}")
elif operacao == 3:
    multiplicacao = num1 * num2
    print(f"A multiplicação de {num1} * {num2} = {multiplicacao}")
elif operacao == 4:
    divisao = num1 / num2
    print(f"A divisão de {num1} / {num2} = {divisao}")
else:
    print("Número digitado para realizar a operação é incorreto!")