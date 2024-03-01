# Zwierzak z właściwością
# Demonstruje właściwości

class Critter(object):
    """Wirtualny pupil"""
    def __init__(self, name):
        print("Urodził się nowy zwierzak.")
        self.__name = name

    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, new_name):
        if(new_name == ""):
            print("pusty łańcuch znków nie możyć imieniem zwierzaka.")
        else:
            self.__name = new_name
            print("Zmiana imienia powiodła się.")



crit = Critter("Reksio")

crit.name = ""

print(crit.name)
