# pierwszy program sprawdza czy liczba jest całkowita

print("Ten program sprawdza czy liczba jest całkowita")


liczba = float(input("podaj liczbę: "))

if(liczba.is_integer() == True):
    print("całfkowita")
else:
    print('inna')

