'''
SESSÃO 5 - Estruturas lógica e condicionais em python

10 - Faça um programa que receba a altura e sexo de uma pessoa e calcule e mostre
seu peso ideal, utilizando as seguintes fórmulas (onde h corresponde á altura):
    * Homens: (72.7 * h) - 58
    * mulheres: (62.1 * h)  - 44.7)
'''

nome = (input("Digite o seu nome: "))
altura = float(input("Digite sua altura: "))
sexo = (input("Digite o seu sexo: 'M' para masculino e 'F' para feminino: "))

if sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"{nome}, seu peso ideal é", peso_ideal)
elif sexo == "M":
    peso_ideal = (72.7 * altura) - 58
    print(f"{nome}, seu peso ideal é", peso_ideal)
else:
    print(f"{nome}, você digitou o sexo errado, tente novamente!")
