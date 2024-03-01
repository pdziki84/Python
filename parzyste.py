# pierwszy program sprawdza czy liczba jest parzysta

print("Ten program sprawdza czy liczba jest parzysta")


liczba = int(input("podaj liczbę: "))

temp = liczba % 2

if(temp == 0):
    print("Liczba jest parzysta")
else:
    print("Liczba jest nieparzysta")
