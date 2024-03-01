##Generator haseł: Stwórz prosty generator haseł,
##który będzie generował losowe hasła o określonej długości.
##Użytkownik powinien móc określić długość hasła.


def generator():
    import random
    
    random.seed()
    r = 0
    
    haslo = ''
    dlugosc = int(input("Podaj dłuość hasła: "))
    temp_dl = dlugosc
    
    while(temp_dl > 0):
        r = random.randint(65, 122)
        if(r in range(91, 96)):
           continue
        else:
            litera = chr(r)
            haslo += litera
            temp_dl -= 1


    print(haslo)




def generatorHasla():
    import random
    import string

    haslo = ''
    dlugosc = int(input("Podaj długość hasła do wygenrowania: "))

    while(dlugosc > 0):
        litera = random.choice(string.ascii_letters + string.digits + string.punctuation)
        haslo += litera
        dlugosc -= 1

    print(haslo)    






#generator()
generatorHasla()
