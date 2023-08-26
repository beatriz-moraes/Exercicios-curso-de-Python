'''
SESSÃO 5 - Estruturas lógica e condicionais em python

37 - As tarifas de certo parque de estacionamento são as seguintes:
    1 e 2 hora = R$1,00 cada
    3 e 4 hora = R$1,40 cada
    5 horas e seguintes = R$2,00 cada

    O número de horas a pagar é sempre inteiro e arredondado por excesso.
    Deste modo, quem estacionar durante 61 minutos pagará por duas horas,
    que é o mesmo que pagaria se tivesse permanecido 120 minutos. Os momentos
    de chegada ao parque e partida deste são apresentado na forma de pares de inteiros,
    representando horas e minutos. Por exemplo, o par 12 50 representará "dez para a uma da tarde".
    Pretende-se criar um programa que, lidos pelo teclado os momentos de chegada e de partida,
    escreva na tela o preço cobrado pelo estacionamento. Admite-se que a chegada e a partida se dão com
    intervalo não superior a 24 horas. Portanto, se uma data hora de chegada for superior á de partida,
    isso não é uma situação de erro, antes significará que a partida ocorreu no dia seguinte ao da chegada.

'''
import math
from datetime import datetime

data_chegada = (input("Qual foi seu horário de chegada: Ex: dd/mm/yyyy hh:mm "))

data_saida = (input("Qual foi seu horário de saída: Ex: dd/mm/yyyy hh:mm "))

data_chegada = datetime.strptime(data_chegada, '%d/%m/%Y %H:%M')
data_saida = datetime.strptime(data_saida, '%d/%m/%Y %H:%M')

diferenca = data_saida - data_chegada
dias = diferenca.days
segundos_totais = diferenca.seconds
horas = segundos_totais // 3600
minutos = (segundos_totais // 60) % 60

horas_parque = dias * 24
horas_parque = math.ceil((minutos + horas * 60) / 60 + horas_parque)

if horas_parque <= 2:
    valor = horas_parque * 1.00
elif horas_parque <= 4:
    valor = horas_parque * 1.40
else:
    valor = horas_parque * 2.00

print(f"O valor do estacionamento durante {horas_parque} horas ficou: R$ {valor}")
