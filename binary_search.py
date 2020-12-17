import random

def binary_search(data, target):
    low=0
    high=len(data)-1
    found=False
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            found=True
            break
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return found


def run():
    data = [random.randint(0, 100) for i in range(10)]
    data.sort()
    print(data)
    target = int(input('What number would you like to find? '))
    found = binary_search(data, target)
    if found == True:
        print(f'The number: {target} is in the list')
    else:
        print(f'The number: {target} is not in the list')



if __name__ == '__main__':
    run()