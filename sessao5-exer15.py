'''
SESSÃO 5 - Estruturas lógica e condicionais em python

15 - Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia
da semana correspondente a este numero. Isto é, domingo se 1, segunda-feira se 2, e assim por diente.
'''

num = int(input("Digite um número inteiro: "))

if num == 1:
    print("Domingo!")
elif num == 2:
    print("Segunda-feira!")
elif num == 3:
    print("Terça-feira!")
elif num == 4:
    print("Quarta-feira!")
elif num == 5:
    print("Quinta-feira!")
elif num == 6:
    print("Sexta-feira!")
elif num == 7:
    print("Sábado!")
else:
    print("O número digitado não corresponde a nenhum dia da semana!")


