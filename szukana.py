#Program który znajduje i wyświetli pozyycję na liście
#pierwszego wystąpienia określonej liczby

liczby = input("Podaj kilka liczb: ")
szukana = input("Podaj liczbę do znaleźienia: ")

for p, x in enumerate(liczby):
    if(x != szukana):
        continue
    else:
        print("Znaleziono liczbę %i na pozycji i" %(x,p+1))
