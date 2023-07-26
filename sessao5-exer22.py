'''
SESSÃO 5 - Estruturas lógica e condicionais em python

22 - Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não
se aposentar. As condições para aposentadoria são:

    * Ter pelo menos 65 anos;
    * Ou ter trabalhado pelo menos 30 anos;
    * Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
'''

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
tempo_trabalhado = float(input("Digite o tempo de serviço que você tem: "))

if idade >= 65 or tempo_trabalhado >= 30 or (idade >= 60 and tempo_trabalhado >= 25):
    print(f"{nome}, você já pode aposentar!")
else:
    print(f"{nome}, você ainda não pode aposentar!")
