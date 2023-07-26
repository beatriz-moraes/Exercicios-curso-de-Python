'''
SESSÃO 5 - Estruturas lógica e condicionais em python

19 - Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5.
mas não simultaneamente pelos dois.
'''

num = int(input("Digite um número inteiro:"))

if num % 3 != 0 and num % 5 != 0:
    print("O número digitado não divisível por 3 e 5 simultaneamente!")
elif num % 3 == 0 and num % 5 == 0:
    print("O número digitado é divisível por 3 e 5 simultaneamente!")
elif num % 3 == 0:
    print("O número digitado é divisível por 3!")
elif num % 5 == 0:
    print("O número digitado é divisível por 5!")
