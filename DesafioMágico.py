# Importamos la biblioteca random
import random

# Variables para almacenar los datos
quidditch_events = ["goal", "goal", "snitch", "goal", "foul", "goal"]
gryffindor_score = 0
slytherin_score = 0

# Bucle para procesar los eventos
for evento in quidditch_events:
    # Actualizamos el marcador de Gryffindor
    if evento == "goal":
        gryffindor_score += 10
    elif evento == "snitch":
        gryffindor_score += 150
    elif evento == "foul":
        gryffindor_score -= 30

    # Actualizamos el marcador de Slytherin
    if evento == "goal":
        slytherin_score += 10
    elif evento == "snitch":
        slytherin_score += 150
    elif evento == "foul":
        slytherin_score -= 20

# Determinamos el ganador
if gryffindor_score > slytherin_score:
    ganador = "Gryffindor"
elif slytherin_score > gryffindor_score:
    ganador = "Slytherin"
else:
    ganador = "Empate"

# Imprimimos los resultados
print("Puntaje de Gryffindor:", gryffindor_score)
print("Puntaje de Slytherin:", slytherin_score)
print("El ganador es:", ganador)
