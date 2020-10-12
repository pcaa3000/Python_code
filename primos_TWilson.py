def factorial(number):
    if number==0:
        return 1
    elif number<3:
        return number
    else:
        return number*factorial(number-1)


def is_prime(number):
    if number<2:
        return False    
    return (factorial(number-1)+1)%number==0    


def run():
    number=int(input("Enter a number: "))    
    if is_prime(number):
        print('Es primo.')
    else:
        print('No es primo.')


if __name__ == "__main__":
    run()
    