##Napisz program „oceny.py”, który wczytuje od użytkownika kolejne oceny i:

## sprawdza czy wprowadzona ocena jest na liście dopuszczalnych na wydziale ocen
## jeżeli ocena jest na liście dopuszczalnych na wydziale ocen,
## dodaje ją na listę otrzymanych ocen
## jeżeli wciśnięto sam Enter, oznacza to koniec listy otrzymanych ocen
## wyświetla wyliczoną dla listy otrzymanych ocen średnią arytmetyczną.


adv = 0
ocena = -2
lista_ocen =[]
dop_oceny = (1, 2, 3, 4, 5, 6)

while(ocena != True):
    ocena = input("Wprowadź ocenę: ")
    if(ocena in dop_oceny):
        lista_ocen.append(ocena)
    elif(ocena == ''):
        adv = sum(lista_ocen)/len(lista_ocen)
        break

    
print("Średnia ocen ucznia wynosi %3.2f: " %adv)
