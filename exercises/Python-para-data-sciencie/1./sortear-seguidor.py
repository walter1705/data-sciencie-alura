# Se debe escribir un programa para sortear a un seguidor de una red social
# para ganar un premio. La lista de participantes está numerada y
# debemos elegir aleatoriamente un número según la cantidad
# de participantes.
#
# Pide a la persona usuaria que proporcione el número de participantes del
# sorteo y devuelve el número sorteado.

from random import randrange as randomize

numero_participantes = int(input("Ingrese la cantidad de participantes del sorteo: ").strip())

ganador = randomize(numero_participantes+1)

print(f'El ganador es el numero : {ganador}')
