# najlepsze wyniki
# Demonstracja metod listy

scores = []
choice = None

while(choice != "0"):
    print("""
            Najlepsze wyniki
            0 - zakończ
            1 - pokaż wyniki
            2 - dodaj wynik
            3 - usuń wynik
            4 - posortuj wyniki
            """
          )

    choice = input("Wybierz: ")
    print()

    #zakończ program
    if(choice == "0"):
        print("Do widzenia.")
    #wypisz wyniki
    elif(choice == "1"):
        print("najlepsze wyniki: ")
        for score in scores:
            print(score)
    #dodaj wynnik
    elif(choice == "2"):
        score = int(input("Jaki wynik uzyskałeś: "))
        scores.append(score)
    #usuń wynik
    elif(choice == "3"):
        score = int(input("Który wynik usunąć: "))
        if(score in scores):
            scores.remove(score)
        else:
            print(score, "NIe ma na liście wyników.")
    #posortuj wyniki
    elif(choice == "4"):
                scores.sort(reverse = True)
    #postępowanie po nieprawidłowym wyborze
    else:
        print("niestety,", choice, "nie jest prawidłowym wyborem.")















































    
    


