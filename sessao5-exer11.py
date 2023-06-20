'''
SESSÃO 5 - Estruturas lógica e condicionais em python

11 - Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a
soma de todos seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2+5+1).
Se o número lido não for maior do que zero, o programa terminará com a mensagem "Número inválido"
'''

num = int(input("Digite um número inteiro maior do que zero: "))

if num > 0:
    soma = 0
    for digito in str(num):
        soma += int(digito)
    print(f"A soma dos algarismos foi: {soma}")
else:
    print("Número inválido!")
