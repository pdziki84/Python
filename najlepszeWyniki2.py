#Najlepsze wyniki 2.0
# demonstuje sekwencje zagnieżdzone

scores = []
choice = None

while(choice != 0):
    print("""
        Najlepsze wyniki 2.0

        0 - zakończ
        1 - wyświetl wyniki
        2 - dodaj wynik
        """
          )
    choice = input("wybierz opcje: ")
    print()
    
    #zakończ
    if(choice == "0"):
        print("Do widzenia.")
        break
    #wyświetl tabele najlepszych wyników
    elif(choice == "1"):
        print("Najlepsze wyniki\n")
        print("GRACZ\tWYNIK")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)
    # add a score
    elif(choice == "2"):
        name = input("Podaj nazwe gracza: ")
        score = int(input("Podaj wynik gracza: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse = True)
        scores = scores[:5] #zachowaj tylkko 5 najlepszych wyników
    else:
        print("Niestety", choice, "nie jest prawidłowym wyborem")
        
input("\nAby kontynuować grę, naciśnij dowolny klawisz.")
