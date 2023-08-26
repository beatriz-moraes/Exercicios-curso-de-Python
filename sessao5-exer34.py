'''
SESSÃO 5 - Estruturas lógica e condicionais em python

34 - Leia a nota e número de faltas de um aluno, e escreva seu conceito. De acordo com a tabela abaixo,
quando o aluno tem mais de 20 faltas ocorre uma redução de conceito.

    NOTA             CONCEITO (ATÉ 20 FALTAS)      CONCEITO (MAIS DE 20 FALTAS)
9.0 até 10.0                    A                              B
7.5 até 8.9                     B                              C
5.0 até 7.4                     C                              D
4.0 até 4.9                     D                              E
0.0 até 3.9                     E                              E

'''

nota = float(input("Digite sua nota: "))
faltas = int(input("Digite a quantidade de faltas: "))

if nota <= 3.9:
        print("O seu conceito é E")
elif nota <= 4.9:
    if faltas <= 20:
        print("O seu conceito é D")
    else:
        print("O seu conceito é E")
elif nota <= 7.4:
    if faltas <= 20:
        print("O seu conceito é C")
    else:
        print("O seu conceito é D")
elif nota <= 8.9:
    if faltas <= 20:
        print("O seu conceito é B")
    else:
        print("O seu conceito é C")
elif nota <= 10.0:
    if faltas <= 20:
        print("O seu conceito é A")
    else:
        print("O seu conceito é B")
else:
    print("Conceito inexistente!")
