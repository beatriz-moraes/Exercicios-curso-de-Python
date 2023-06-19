'''
SESSÃO 5 - Estruturas lógica e condicionais em python

8 - Faça um programa que leia 2 notas de um ano, verifique se as notas são válidas e
exiba na tela a média destas notas. Uma nota válida deve ser obrigatoriamente, um valor
0.0 e 10.0, onde caso a nota não possua valor válido, este fato deve ser informado ao usuário e o program termina.
'''

nome = input("Seja bem vindo! Qual é o seu nome? ")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua primeira nota: "))

media = (nota1 + nota2) / 2

if 0 < media < 10:
    print(f" {nome}, a média das suas notas foi {media}!")
else:
    print(f"{nome}, as notas informadas não são validas!")
