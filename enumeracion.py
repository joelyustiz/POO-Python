objetivo = int (input('Escode un entero: '))
respuesta = 0
ciclos = 0

while respuesta **2 < objetivo:
    respuesta +=1
    ciclos +=1

if respuesta**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else: 
    print(f'{objetivo} no tiene una raiz cuadrada exacta')

print(ciclos)