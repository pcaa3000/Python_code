objetivo = int(input('Escoge un entero: '))
respuesta = 0

while respuesta**2 < abs(objetivo):
    print(respuesta)
    respuesta += 1

if respuesta**2 == abs(objetivo):
    if objetivo < 0:
        respuesta=-respuesta
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene una raiz cuadrada exacta')