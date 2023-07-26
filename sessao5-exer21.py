'''
SESSÃO 5 - Estruturas lógica e condicionais em python

21 - Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida.
Escreva uma mensagem de erro se a opção for inválida.

Escolha a opção:
1- Soma de 2 números;
2- Diferença entre 2 números (maior pelo menor);
3- Produto entre 2 números;
4- Divisão entre 2 números (o denominador não pode ser zero).
'''

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um número inteiro: "))

opcao = int(input(
                  "1- Soma de 2 números; \n"
                  "2- Diferença entre 2 números (maior pelo menor); \n"
                  "3- Produto entre 2 números; \n"
                  "4- Divisão entre 2 números (o denominador não pode ser zero). \n"
                  "Escolha a opção: "))

if opcao == 1:
    soma = num1 + num2
    print(f"A soma de {num1} + {num2} = {soma}")
elif opcao == 2:
    if num1 > num2:
        diferenca = num1 - num2
        print(f"A diferença entre o {num1} - {num2} = {diferenca}!")
    else:
        diferenca = num2 - num1
        print(f"A diferença entre o {num2} - {num1} = {diferenca}!")
elif opcao == 3:
    produto = num1 * num2
    print(f"A multiplicação entre o {num1} * {num2} = {produto}!")
elif opcao == 4:
    if num2 == 0:
        print("O denominador não pode ser zero!")
    else:
        divisao = num1 / num2
        print(f"A divisão entre o {num1} / {num2} = {divisao}!")
else:
    print("Opção digitada não existe!")
