koniec = int(input("Podaj górną granicę zakresu do wyszukiwania liczb pierwszych: "))

# Inicjalizacja listy pierwsze jako listy długości koniec+1 z wartościami True
pierwsze = [True] * (koniec + 1)

n = 2
while(n <= koniec):
    if(pierwsze[n] == True):
        m = n * 2
        while(m <= koniec):
            pierwsze[m] = False
            m += n
    n += 1

print("Znalezione liczby pierwsze:")
for n in range(2, koniec + 1):
    if(pierwsze[n] == True):
        print(n, end=' ')



