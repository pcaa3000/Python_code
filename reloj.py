ms = 0
s = 0
min = 0
hr = 24

while hr < 24:
    while min < 60:
        while s < 60:
            while ms < 1000:
                print(f'{hr} hr : {min} min : {s} s : {ms} ms')
                ms += 1
            s += 1
            ms = 0
        min += 1
        s = 0
    hr += 1
    min = 0
print(f'{hr} hr : {min} min : {s} s : {ms} ms')