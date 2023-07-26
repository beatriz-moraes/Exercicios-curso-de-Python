'''
SESSÃO 5 - Estruturas lógica e condicionais em python

27 - Escreva um programa que, dada a idade de um nadador,  classifique-o em uma das seguintes categorias:

            CATEGORIAS      IDADE
            Infantil A      5 a 7
            Infantil B      8 a 10
            Juvenil A       11 a 13
            Juvenil B       14 a 17
            Sênior          Maiores de 18 anos
'''

idade = int(input("Digite a sua idade: "))

if idade >= 5 and idade <= 7:
    print("Categoria Infantil A!")
elif idade <= 10:
    print("Categoria Infantil B!")
elif idade <= 13:
    print("Categoria Juvenil A!")
elif idade <= 17:
    print("Categoria Juvenil B!")
elif idade >= 18:
    print("Maiores de 18 anos!")
