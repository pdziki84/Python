# Pogromca obcych
#Demonstruuje współdziałanie obiektów

class Player(object):
    """Gracz w grze strzelance"""
    def blast(self, enemy):
        print("Gracz razi wroga i wyrywa mu język bo za głośno wrzeszczys\n")
        enemy.die()
        
    def oboz(self, enemy):
        print("Bohater zbudował obóz koncentracyjny dla obcych")
        enemy.burn()

class Alien(object):
    """Obcy w grze strzelance"""
    def die(self):
        print("Obcy z trudem łapie oddech, 'To już koniec. Ale wielki koniec... \n" 
                "Tak, już robi się ciemno. Powiedz moim dwóm milionom larw, że je\
                    kochałem... \n" \
                "Żegnaj, okrutny Wszechświecie. chciał powiedzieć ale już nie mógł'")
    def burn(self):
        print("Płoniemy jak żydzi w Auswitz tylko, że na żywca.")


#main
print("\t\tŚmierć Obcefo\n")

hero = Player()
invandor = Alien()

hero.oboz(invandor)
hero.blast(invandor)


input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
