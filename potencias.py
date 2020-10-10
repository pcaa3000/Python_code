def pow2(limit,exp):
    if limit >= 2**exp:
        print(f'2 elevado a la {exp} es {2**exp}')
        pow2(limit,exp+1)           


def run():
    limit=int(input('Ingresar el limite máximo de las potencias de 2: '))    
    pow2(limit, 0)


if __name__ == '__main__':
    run()