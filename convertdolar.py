exchange=3.59

print("Money exchange\n")
money=float(input("Ingresa la cantidad de soles: "))

dolar= round(money/exchange,2)
print(f'Al cambio tendrías {dolar} dolares.\n')
