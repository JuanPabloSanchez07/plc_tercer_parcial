# error_sensor.py

# Import the math and random modules
import math
import random

# Variables to store the data
lecturas = []
errores = []

# Loop to read sensor readings
for i in range(100):
    lectura = math.floor(random.random() * 50) + 10
    lecturas.append(lectura)

# Detect incorrect readings
for lectura in lecturas:
    if lectura < 10 or lectura > 40:
        errores.append(lectura)

# Calculate the error percentage
porciento_errores = len(errores) / len(lecturas) * 100

# Print the result
print(f"The error percentage is {porciento_errores:.2f}%")
