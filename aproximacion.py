from time import time
objetivo = int(input('Escoge un numero: '))
epsilon = 0.0001
paso = epsilon**2 
respuesta = 0.0

time_initial=time()
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso

total_time=time()-time_initial
ṕ
if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada {objetivo}')
else:
    print(f'La raiz cudrada de {objetivo} es {respuesta}')
print(f'Respuesta demoro: {total_time} segundos')