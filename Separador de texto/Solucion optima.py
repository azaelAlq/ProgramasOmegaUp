# Inicializar la lista de entrada
entrada = []

# Leer la entrada hasta que se ingrese "-1"
while True:
    var = input()
    if var == "-1":
        break
    entrada.append(var)

# Concatenar los elementos de la lista con " -> "
resultado = " -> ".join(entrada)

# Imprimir el resultado
print(resultado)
