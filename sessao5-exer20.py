'''
SESSÃO 5 - Estruturas lógica e condicionais em python

20 - Dados três valores, A,B,C, verificar se eles podem ser valores dados de um triângulo e, se forem,
se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:

    * O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados;
    * Chama-se equilátero o triângulo que tem três lados iguais;
    * Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
    * Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
'''

valor_A = float(input("Digite o valor de A: "))
valor_B = float(input("Digite o valor de B: "))
valor_C = float(input("Digite o valor de C: "))

if valor_A + valor_B > valor_C and valor_A + valor_C > valor_B and valor_B + valor_C > valor_A:
    if valor_A == valor_B and valor_A == valor_C:
        print("O triângulo é o equilátero!")
    elif valor_A != valor_B and valor_A != valor_C:
        print("O triângulo é o escaleno!")
    elif valor_A == valor_B or valor_A == valor_C or valor_B == valor_C:
        print("O triângulo é o isósceles!")
else:
    print("Os valores informados não são dados de um triângulo!")