estudiantes = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4,
}

for pais in estudiantes:
    print(pais)
    #print(type(pais))

for pais in estudiantes.keys():
    print(pais)

for numero_de_estudiantes in estudiantes.values():
    print(numero_de_estudiantes)

for pais, numero_de_estudiantes in estudiantes.items():
    print(pais,numero_de_estudiantes)

matriz=[[1,2,3],[4,5,6],[7,8,9]]
for fila in matriz:
    for elemento in fila:
        print(elemento)