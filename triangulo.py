def asknumber (message):
    number=int(input(f'{message}'))
    while number <= 0:
        print('Ingrese números mayores a cero')
        number=int(input(f'{message}'))
    return number

def validetriangle(sides):    
    if sides[0]+sides[1]>sides[2] and sides[2]+sides[0]>sides[1] and sides[1]+sides[2]>sides[0]:
        return True
    else:
        return False

def typetriangle(sides):
    area=0
    if sides[0]==sides[1] and sides[0]==sides[2]:
        print('Triángulo Equilatero')
        area=findheighteq(sides[0])*sides[0]/2
    elif sides[0]==sides[1] or sides[0]==sides[2] or sides[1]==sides[2]:
        if sides[0]==sides[1]:
            base=sides[2]
            height=findheightis(base,sides[0])
        elif sides[0]==sides[2]:
            base=sides[1]
            height=findheightis(base,sides[0])
        else:
            base=sides[0]
            height=findheightis(base,sides[1])
        print('Triángulo Isoseles')
        area=height*base/2
    else:
        print('Triángulo Escaleno')
        semiperimeter=0
        for side in sides:
            semiperimeter+=side
        semiperimeter=semiperimeter/2
        area=semiperimeter
        for side in sides:
            area*=(semiperimeter-side)
        area=area**(1/2)
    print(f'El área del Triángulo es: {area}')

def findheighteq(side):
    return (side/2)*(3**(1/2))

def findheightis(base,side):
    return (side**2-(base/2)**2)**(1/2)

print('Ingresar los lados del Tringulo\n')
sidesnumber=3
sides=[1,1,1]
for index in range(sidesnumber):
    sides[index]=asknumber(f'Ingresar el {index+1}° lado: ')

if not validetriangle(sides):
    print('Triangulo no valido')
    exit()

typetriangle(sides)
