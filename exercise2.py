import random
msg='Hola, Este programa te dirá si eres mayor, menor o si tienes la misma edad que Mr. Robot'
print(f'{ "-" *len(msg)}')
print(msg)
print(f'{"-"*len(msg)} \n')
name_user=input('Ingresa tu nombre: ')
age_user=int(input('Ingresa tu edad: '))
age_mrrobot=random.randrange(100)

print(f'\n{name_user} tienes {age_user} año(s) y Mr. Robot tiene {age_mrrobot} año(s)')
msg='Por lo tanto, '
if age_user>age_mrrobot:
    print(f'{msg}{name_user} eres mayor que Mr. Robot')
elif age_user<age_mrrobot:
    print(f'{msg}{name_user} eres menor que Mr. Robot')
else:
    print(f'{msg}{name_user} tienes la misma edad que Mr. Robot')
