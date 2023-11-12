# Asistente.py

# Función para detectar si se escribe Alexa en un texto
def contiene_alexa(texto):
      return "alexa" in texto.lower().split()

# Entrada del usuario
texto = input("Ingrese un texto: ")

# Detectamos si se escribe Alexa
if contiene_alexa(texto):
      print("Tranquilo, solo di mi nombre una vez")
else:
      print("No se ha escrito Alexa")
