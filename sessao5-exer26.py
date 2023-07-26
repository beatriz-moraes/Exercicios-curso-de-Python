'''
SESSÃO 5 - Estruturas lógica e condicionais em python

26 - Leia a distância em km e a quantidade de litros de gasolina consumidos  por um  carro em um percurso,
calcule o consumo em km/l e escreva uma mensagem  de acordo com a tabela abaixo:

    *CONSUMO     KM/L   MENSAGEM
    Menor que    8      venda o carro!
    Entre      8 e 12   Econômico!
    Maior que   14      Super econômico!

Consumo (km/l) = Distância percorrida (km) / Quantidade de gasolina consumida (litros)
'''

gasolina = float(input("Digite a quantidade de litros de gasolina consumido: "))
distancia = float(input("Digite a distância em km pelo percurso: "))

consumo = distancia / gasolina

if consumo < 8:
    print("Venda o carro!")
elif consumo < 12:
    print("Econômico!")
else:
    print("Super econômico!")
