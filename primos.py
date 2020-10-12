def is_prime(number):
    if number<2:
        return False
    prime=True
    for i in range(2,number):
        if number%i==0:
            prime=False
            break
    return prime



def run():
    number=int(input("Enter a number: "))
    if is_prime(number):
        print('Es primo.')
    else:
        print('No es primo.')


if __name__ == "__main__":
    run()
    