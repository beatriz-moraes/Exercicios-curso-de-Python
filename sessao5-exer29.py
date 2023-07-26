'''
SESSÃO 5 - Estruturas lógica e condicionais em python

29 - Faça uma prova de matemática para crianças que estão aprendendo a  somar  números
inteiros menores do que 100. Escolha números aleatórios entre 1 e 100, e mostre na tela a pergunta:
qual é a soma de a + b, onde a e b são números aleatórios. Peça a resposta. Faça cinco perguntas ao aluno,
e mostre para ele as perguntas e respostas corretas, além  de quantas vezes o aluno acertou.
'''
import random
nome = input("Qual o seu nome: ")
print(f"Seja bem vinda {nome}, vamos jogar?!")

acertos = 0

for i in range(5):
    numero_aleatorio_a = random.randint(1, 100)
    numero_aleatorio_b = random.randint(1, 100)
    soma = numero_aleatorio_a + numero_aleatorio_b

    reposta_aluna = float(input(f"Quanto é {numero_aleatorio_a} + {numero_aleatorio_b}? "))

    if reposta_aluna == soma:
        print(f"Parabéns {nome}, você acertou!")
        acertos += 1
    else:
        print(f"Infelizmente você não acertou, a resposta correta era: {soma}")

if acertos >= 3:
    print(f"\nVocê foi incrível, acertou {acertos} perguntas!")
else:
    print(f"\nVocê precisa estudar um pouco mais, acertou {acertos} perguntas!")