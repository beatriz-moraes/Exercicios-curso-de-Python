'''
SESSÃO 5 - Estruturas lógica e condicionais em python

25 - Calcule as raízes da equação do segundo grau.

A variável a tem que ser diferente de zero. Caso seja igual, imprima a mensagem "Não é equação de segundo grau".
    *Se delta < 0, não existe real. Imprima a mensagem "Não existe raiz";
    * Se delta = 0, existe uma raiz real. Imprima a raiz e a mensagem "Raiz única"
    * Se delta >= 0 , imprima as duas raízes reais.
'''

a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))

delta = b * b - 4 * a * c


x1 = (-b + delta ** 1/2) / (2 * a)
x2 = (-b - delta ** 1/2) / (2 * a)

x1_grau = a * (x1 * x1) + (b * x1) + c
x2_grau = a * (x2 * x2) + (b * x2) + c

if x1_grau == 0 and x2_grau == 0:
    print("Representa uma equação do segundo grau!")

if delta < 0:
    print("Não existe raiz!")
elif delta == 0 and (isinstance(x1, float) or isinstance(x2, float)):
    print("Raiz única!")
elif delta >= 0 and (isinstance(x1, float) and isinstance(x2, float)):
    print(f"x1:{x1} e x2:{x2}")
