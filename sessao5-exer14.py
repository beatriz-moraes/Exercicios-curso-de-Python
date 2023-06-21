'''
SESSÃO 5 - Estruturas lógica e condicionais em python

13 - Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda
prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno
foi aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos.
'''

nome = (input("Digite o seu nome:"))
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))

soma = (nota1 + nota2 + (nota3 * 2)) / 4

if soma >= 60:
    print(f"{nome}, Parabéns! Você está aprovado!")
else:
    print(f"{nome}, infelizmente você está reprovado!")

