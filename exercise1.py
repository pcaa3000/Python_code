# Ejercicio sobre cadenas
my_name=input('Me indicas tu nombre: ')
tweet=f'Hola {my_name}, como estas, Bienvenido a Platzi.'
tamanio_tweet=len(tweet)
print(f'{"_"*30}')
print('@python')
print(f'{"-"*tamanio_tweet}')
print(tweet)
print(f'{"-"*tamanio_tweet}')
print(f'Sabías que el tweet anterior tiene {tamanio_tweet} caracteres de los 280 permitidos')
