'''
SESSÃO 5 - Estruturas lógica e condicionais em python

4 - Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
    * O número digitado ao quadrado.
    * A raiz quadrada do número digitado
'''
import math

num = int(input("Digite um número: "))

if num >= 0:
    num_ao_quadrado = math.pow(num, 2)
    raiz_quadrada = math.sqrt(num)
    
    print(f"O número que foi digitado ao quadrado é: {num_ao_quadrado}")
    print(f"A raiz quadrada do número digitado é: {raiz_quadrada}")
else:
    print("Por favor, digite um número positivo(números acima de zero)!")
