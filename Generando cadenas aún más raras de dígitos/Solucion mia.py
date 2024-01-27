import random

TamañoCadena = input()

CadenaSalida = ""

for i in range(int(TamañoCadena)):
    CadenaSalida += str(random.randint(0, 9))

print(CadenaSalida)
