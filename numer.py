# program zmienia cyfre na napis


list_strings = ["zero", "jeden", "dwa", "trzy", "cztery", "pięć",
                "sześć", "siedem", "osiem", "dziewięć"]


liczba = input("Podaj liczbę całkowitą do przetworzenia: ")
wynik = ''

for cyfra in liczba:
    if(cyfra.isdigit()):
        wynik +=list_strings[int(cyfra)] + ' '

print(wynik.strip())












    

