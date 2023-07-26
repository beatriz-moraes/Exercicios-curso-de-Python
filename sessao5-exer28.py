'''
SESSÃO 5 - Estruturas lógica e condicionais em python

28 - Faça  um  programa  que leia  três números positivos e efetue o cálculo de uma das
seguintes médias de acordo com um valor numérico digitado pelo usuário:

        (a) Geométria: raiz cubica de (x * y * z)
        (b) Ponderada: (x + 2 * y + 3 * z) / 6
        (c) Harmônica: 1 / (1/x + 1/y + 1/y)
        (d) Aritmética: (x + y + z) / 3
'''
operacao = input("(a) Geométria\n"
                "(b) Ponderada \n"
                "(c) Harmônica \n"
                "(d) Aritmética \n"
                "Escolha a operação desejada: ")

x = float(input("Digite o primeiro número positivo: "))
y = float(input("Digite o segundo número positivo: "))
z = float(input("Digite o terceiro número positivo: "))

if operacao == 'a':
    calculo = (x * y * z) ** (1/3)
    print(f"Resultado da Geometria: {calculo}")
elif operacao == 'b':
    calculo = (x + 2 * y + 3 * z) / 6
    print(f"Resultado da Ponderada: {calculo}")
elif operacao == 'c':
    calculo = 1 / (1/x + 1/y + 1/y)
    print(f"Resultado da Harmônica: {calculo}")
elif operacao == 'd':
    calculo = (x + y + z) / 3
    print(f"Resultado da Aritmética: {calculo}")
else:
    print("Operação escolhida não existe!")
