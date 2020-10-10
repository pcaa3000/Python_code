def palindromo(word):
    word=word.replace(' ','').lower()
    return word == word[::-1]


def run():
    word=input('Ingrese una palabra: ')
    if palindromo(word) == True:
        print(f'Es palídromo')
    else:
        print(f'No es palídromo')


if __name__ == '__main__':
    run()
