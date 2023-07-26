'''
SESSÃO 5 - Estruturas lógica e condicionais em python

24 - Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente
de imposto sobre o produto (MG 7%, SP 12%, RJ 15%, MS 8%). Faça um programa em que o usuário entre com valor
e o estado destino do produto e o programa retorne o preço final do produto acrescido  o imposto do estado
que que será vendido. Se o estado digitado não for válido, mostrar uma mensagem de erro.
'''

valor = float(input("Digite o valor do produto: "))
estado = int(input("Digite o estado destino do produto: (1- RJ, 2- SP, 3- MG, 4- MS): "))

if estado == 1:
    imposto = (valor * 15 / 100) + valor
    print(f"O valor do produto com o imposto para o estado do RJ é: {imposto}!")
elif estado == 2:
    imposto = (valor * 12 / 100) + valor
    print(f"O valor do produto com o imposto para o estado de SP é: {imposto}!")
elif estado == 3:
    imposto = (valor * 7 / 100) + valor
    print(f"O valor do produto com o imposto para o estado de MG é: {imposto}!")
elif estado == 4:
    imposto = (valor * 8 / 100) + valor
    print(f"O valor do produto com o imposto para o estado de MS é: {imposto}!")
else:
    print("Estado digitado é inválido!")
