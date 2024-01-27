Entrada = []
contador = 0
cadena = ""
var = ""

while var != "-1":
    var = input()
    Entrada.append(var)

while Entrada[contador] != "-1":
    cadena += Entrada[contador]

    if Entrada[contador + 1] != "-1":
        cadena += " -> "

    contador += 1

print(cadena)
