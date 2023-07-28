'''
SESSÃO 5 - Estruturas lógica e condicionais em python

31 - Calcule as raízes da equação do segundo grau.

Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir, verifique
e mostre qual a classificação dessa pesssoa.

  Altura                          Peso
                    Até 60    Entre 60 e 90 (inclusive)    Acima de 90
  Menor que 1,20      A                   D                     G
  De 1,20 a 1,70      B                   E                     H
  Maior que 1,70      C                   F                     I

'''

nome = input("Digite o seu nome: ")
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

if altura < 1.20:
    if peso < 60:
        print(f"{nome}, sua classificação é A! ")
    elif peso > 90:
        print(f"{nome}, sua classificação é G! ")
    else:
        print(f"{nome}, sua classificação é D! ")
elif altura > 1.70:
    if peso < 60:
        print(f"{nome}, sua classificação é B! ")
    elif peso > 90:
        print(f"{nome}, sua classificação é H! ")
    else:
        print(f"{nome}, sua classificação é E! ")
else:
    if peso < 60:
        print(f"{nome}, sua classificação é C! ")
    elif peso > 90:
        print(f"{nome}, sua classificação é F! ")
    else:
        print(f"{nome}, sua classificação é I! ")

