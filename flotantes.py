x = 0.0
for i in range(10):
    x += 0.1
    print(f'{i}: {x}')
    #if x <= 1.0 and x>0.99999:
if x==1.0:
    print(f'x = {x}')
else:
    print(f'x != {x}')