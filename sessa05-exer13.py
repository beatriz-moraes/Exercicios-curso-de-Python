'''
SESSÃO 5 - Estruturas lógica e condicionais em python

14 - A nota final de um estudante é calculada a partir de três notas atribuidas entre o intervalo
de 0 até 0, respectivamente, um trabalho de laboratório, uma avaliação semestral e a um exame final.
A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de laboratório: 2;
Avaliação semestral: 3; Exame final: 5. De acordo com o resultado, mostre na tela se o aluno está
reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado.
faça todas verificações necessárias.
'''

nome = (input("Digite o seu nome:"))
nota1 = float(input("Digite a primeira nota( 0 a 10): "))
nota2 = float(input("Digite a segunda nota( 0 a 10): "))
nota3 = float(input("Digite a terceira nota( 0 a 10): "))

soma = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10

if soma <= 2.9:
    print(f"{nome}, infelizmente você está reprovado!")
elif soma <= 4.9:
    print(f"{nome}, infelizmente você está de recuperação!")
else:
    print(f"{nome}, Parabéns! Você foi aprovado!")
