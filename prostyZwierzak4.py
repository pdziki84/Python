# Prywatny zwierzak
# Demonstruje zmienne i metody prywatne

class Critter(object):
    """Wirtualny pupil"""
    def __init__(self, name, mood):
        print("Urodził się nowy zwierzak")
        self.name = name            #atrybut publicznny
        self.__mood = mood          #atrybut prywatny


    def talk(self):
        print("\nJestm ", self.name)
        print("W tej chwili czuję się", self.__mood, "\n")





crit = Critter(name = "Reksio", mood = "szczęśliwy")
