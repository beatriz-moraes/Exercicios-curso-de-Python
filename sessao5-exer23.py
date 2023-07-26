'''
SESSÃO 5 - Estruturas lógica e condicionais em python

23 - Determine se um denominado ano lido é bissexto. Sendo que um ano é bissexto se for divisível por 400
ou se for divisível por 4 e não for divisível por 100. Por exemplo: 1988, 1992, 1996.
'''

ano = int(input("Digite um ano: "))

if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print(f"O ano {ano} é bissexto!")
else:
    print(f"O ano {ano} não é bissexto!")
