'''
SESSÃO 5 - Estruturas lógica e condicionais em python

9 - Leia o salário de um trabalhador e o valor da prestação de um empréstimo.
Se a prestação for maior que 20% do salário imprima: 'Empréstimo não concedido', caso
contrário imprima 'Empréstimo concedido'
'''

nome = input("Digite o seu nome: ")
salario = float(input("Digite o seu salário: "))
emprestimo = float(input("Digite o valor do emprestimo que deseja fazer: "))

prestacao = (salario * 20) / 100

if emprestimo > prestacao:
    print(f"{nome}, infelizmente seu empréstimo não foi concedido!")
else:
    print(f"{nome}, o seu empréstimo foi concedido!")

