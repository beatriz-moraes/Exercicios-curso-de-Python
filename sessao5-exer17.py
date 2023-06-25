'''
SESSÃO 5 - Estruturas lógica e condicionais em python

17 - Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
A = (base_maior + base_menor) * altura / 2. Lembre-se a base maior e a base menor devem ser números maiores que zero.
'''

base_maior = float(input("Digite a base maior(sendo ele maior que zero): "))
base_menor = float(input("Digite a base menor(sendo ele maior que zero): "))
altura = float(input("Digite a altura: "))

trapezio = (base_maior + base_menor) * altura / 2

print(f"A área do trapézio é: {trapezio}")
