lista_ocen = []

while True:
    ocena_str = input("Wprowadź ocenę (lub wciśnij Enter, aby zakończyć): ")
    if(ocena_str == ""):
        break
    try:
        ocena = int(ocena_str)
        if(ocena in range(1, 7)):
           lista_ocen.append(ocena)
        else:
            print("Nieprawidłowa ocena. Proszę prowadzić liczbę od 1 do 6.")
    except ValueError:
        print("Nieprawidłowy format oceny. proszę wprowadzić liczbę od 1 do 6")

if(lista_ocen):
    srednia = sum(lista_ocen) / len(lista_ocen)
    print("Średnia ocen ucznia wynosi {:.2f}".format(srednia))
else:
    print("Nie wprowadzono żadnych ocen")
