from time import time


objetivo = int(input('Escoge un numero: '))
epsilon = 0.0001
bajo = 0.0
alto = max(1.0, objetivo)
respuesta = (alto + bajo) / 2

time_initial=time()
while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta

    respuesta = (alto + bajo) / 2
total_time=time()-time_initial

print(f'La raiz cuadrada de {objetivo} es {respuesta}')
print(f'Tiempo de respuesta {total_time} segundos.')