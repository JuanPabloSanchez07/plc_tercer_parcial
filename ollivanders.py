# Ollivanders.py

# Importamos el módulo random
import random

# Listas para almacenar los datos
clientes = []
varitas = []

# Bucle para registrar los clientes
while True:
      nombre = input("¿Cuál es su nombre? ")
      clientes.append(nombre)

    # Preguntamos si el cliente quiere comprar una varita
      respuesta = input("¿Desea comprar una varita? (s/n) ")
      if respuesta == "s":
                # Preguntamos al cliente qué tipo de varita quiere
                tipo_varita = input("¿Qué tipo de varita desea? (1-4)\nLas opciones son:\n1. Varita de Saúco\n2. Varita de Espino\n3. Varita de Sauce\n4. Varita de Acebo\n")
                varita = int(tipo_varita)

          # Verificamos que el tipo de varita sea válido
                if varita >= 1 and varita <= 4:
                              varitas.append(varita)
      else:
                    print("El tipo de varita debe ser un número entre 1 y 4")

      # Preguntamos si hay más clientes
      respuesta = input("¿Hay más clientes? (s/n) ")
      if respuesta == "n":
                break
# Imprimimos el resumen
print("Resumen de ventas")
for i in range(len(clientes)):
      print(f"{clientes[i]} compró una varita {varitas[i]}")

# Calculamos el porcentaje de varitas vendidas
porciento_varitas_vendidas = len(varitas) / len(clientes) * 100
print(f"El porcentaje de varitas vendidas es {porciento_varitas_vendidas:.2f}%")
