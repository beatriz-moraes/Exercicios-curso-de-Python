'''
SESSÃO 5 - Estruturas lógica e condicionais em python

32 - Escrever um programa que leia o código do produto escolhido do cardápio de uma
lanchonete e a quantidade. O programa deve calculcar o valor a ser pago por aquele lanche.
Considere que a cada execução somente será calculado um pedido. O cardápiop da lanchonete segue
o padrão abaixo:

                            Especificação       Código      Preço
                            Cachorro quente     100         1.20
                            Bauru Simples       101         1.30
                            Bauru com ovo       102         1.50
                            Hamburguer          103         1.20
                            Cheeseburguer       104         1.70
                            Suco                105         2.20
                            Refrigerante        106         1.00
'''

print("\n                        CARDÁPIO: \n\n"
                  "Especificação       Código      Preço \n"
                   "Cachorro quente     100         1.20 \n"
                   "Bauru Simples       101         1.30 \n"
                   "Bauru com ovo       102         1.50 \n"
                   "Hamburguer          103         1.20 \n"
                   "Cheeseburguer       104         1.70 \n"
                   "Suco                105         2.20 \n"
                   "Refrigerante        106         1.00 \n")

opcao = int(input("Qual código do lanche desejado: "))
quantidade = int(input("Qual a quantidade do lanche desejado: "))

if opcao == 100:
    qtd = 1.20 * quantidade
    print(f"Você escolheu {quantidade} unidades de cachorro quente! \n"
          f"Valor total foi: R$ {qtd}.")
elif opcao == 101:
    qtd = 1.30 * quantidade
    print(f"Você escolheu {quantidade} unidades de Bauru Simples! \n"
          f"Valor total foi: R$ {qtd}.")
elif opcao == 102:
    qtd = 1.50 * quantidade
    print(f"Você escolheu {quantidade} unidades de Bauru com ovo! \n"
          f"Valor total foi: R$ {qtd}.")
elif opcao == 103:
    qtd = 1.20 * quantidade
    print(f"Você escolheu {quantidade} unidades de Hamburguer! \n"
          f"Valor total foi: R$ {qtd}.")
elif opcao == 104:
    qtd = 1.70 * quantidade
    print(f"Você escolheu {quantidade} unidades de Cheeseburguer! \n"
          f"Valor total foi: R$ {qtd}.")
elif opcao == 105:
    qtd = 2.20 * quantidade
    print(f"Você escolheu {quantidade} unidades de Suco! \n"
          f"Valor total foi: R$ {qtd}.")
elif opcao == 106:
    qtd = 1.00 * quantidade
    print(f"Você escolheu {quantidade} unidades de Refrigerante! \n"
          f"Valor total foi: R$ {qtd}.")