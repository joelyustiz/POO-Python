objetivo = int(input('Escoge un número: '))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objectivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso

if abs(respuesta**2 - objectivo) >= epsilon:
    print(f'No se encontró la Raiz cuadrada del objectivo')
else:
    print(f'La raiz cuadrada de: {objetivo} es {respuesta}')
    