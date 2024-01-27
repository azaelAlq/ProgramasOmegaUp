# Inicializar la cadena y leer la entrada hasta que se ingrese "-1"
cadena = ""
while True:
    var = input()
    if var == "-1":
        break
    cadena += var + " -> "

# Eliminar el último " -> " si existe
if cadena.endswith(" -> "):
    cadena = cadena[:-4]

# Imprimir el resultado
print(cadena)
