#Prosty zwierzak z konstruktorem 
#Demonstracja podstawowej klasy i obiektuvi konstruktora

class Critter(object):
    """Wirtuaalny pupil"""

    def __init__(self):
        print("Urodził się nowy zwierzak")

    def talk(self):
        print("Cześć! Jestem egzemplarzem klasy Critter.")




#Częśc główna

crit1 = Critter()
crit2 = Critter()

crit1.talk()
crit2.talk()


input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
