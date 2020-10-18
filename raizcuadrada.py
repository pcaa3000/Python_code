from time import time


def binary_alg(number, epsilon=0.001):
    low = 0.0
    high = max(1.0, number)
    result = (high + low) / 2
    time_initial=time()
    while abs(result**2 - number) >= epsilon:
        if result**2 < number:
            low = result
        else:
            high = result
        result = (high + low) / 2
    total_time=time()-time_initial
    print(f'La raiz cuadrada de {number} es {result}')
    print(f'Tiempo de respuesta {total_time} segundos.')


def approximation_alg(number,epsilon=0.001):
    result=0.0
    time_initial=time()
    while abs(result**2-number) >= epsilon and result<=number:
        result+=epsilon
    total_time=time()-time_initial
    if abs(result**2-number) >= epsilon:
        print(f'No se encontro la raiz cuadrada {number}')
    else:
        print(f'La raiz cudrada de {number} es {result}')
    print(f'La respuesta demoro: {total_time} segundos')


def enumeration_agl(number):
    result = 0
    time_initial=time()
    while result**2 < abs(number):    
        result += 1
    total_time=time()-time_initial
    if result**2 == abs(number):
        if number < 0:
            result=-result
        print(f'La raiz cuadrada de {number} es {result}')
    else:
        print(f'{number} no tiene una raiz cuadrada exacta')
    print(f'La respuesta demoro: {total_time} segundos')


def run():
    menu="""
    Escoga un método para calcular la raiz cuadrada
        [1] Enumeración
        [2] Aproximación
        [3] Binario
        [0] Salir        
    
    Su opción es: """
    Exit=False
    while not Exit:
        option=int(input(menu))
        if option<0 or option>3:
            print("Option no valida.")
            continue 
        if option==0:
            Exit=True
            continue
        number=int(input("\tIngrese la raíz a calcular : "))
        if option==1:
            enumeration_agl(number)
        elif option==2:
            approximation_alg(number)
        elif option==3:
            binary_alg(number)        


if __name__ == "__main__":
    run()