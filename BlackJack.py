##Rozdaj na początek wszystkim graczom i rozdającemu po 2 karty
##Dla każdego gracza
##    Dopuki raacz prosi o dodarkową kartę i nie ma fury
##        Wydaj graczowi dodatkową kartę
##Jeżeli nie ma już graczy pozostających w grze
##    Pokaż 2 karty rozdającemu
##W przeciwnym wypadku
##    Dopuki rozdający musi dobierać arty i nie ma fury
##        Wydaj rozdającemu dodatkową kartę
##    Jeśli rozdający ma furę
##        Dla każdego gracza pozostającego w grze
##            Graczz wygrywa
##    W pprzeciwnym razie
##        Dla każdego gracza pozostającego w grze
##            Jeśli suma punktów graczza jest większa niz suma punktów rozdającego
##                gracza wygrywa
##            w pprzeciwnym razie, jesli suma gracza jest mniejsza niż suma rozdającego
##                gracz przegrywa
##            w przeciwnym razie
##                gracz remisuje
##
##


#BlackJack
#Od 1 do 7 graczt współzawodniczy z rozdającym

import karty, gry

class BJ_Card(karty.Card):
    """Karta do blackjacka."""
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
            else:
                v = None
            return v

class BJ_Deck(karty.Deck):
    """Talia kart do blackjacka."""
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))

class BJ_Hand(karty.Hand):
    """Ręka w blackjacku"""
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        #Jeśli karta w reće ma wartość None to i wartośc sumy wynosi None
        for card in self.cards:
            if not card.value:
                return None
        # sumuj wartosci kart, traktuj każdego asa jakoo 1
        t = 0
        for card in self.cards:
            t += card.value

        #ustal, czzy ręka zawiera assa
        contains_ace = False

        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        # jeśli reka zawiera asa a suma jest wystarczajaco niska
        # potraktuj asa jako 11

        if contains_ace and t <= 11:
            #dodaj tylko 10, ponieważ już dodaliśmy 1 za asa
            t += 10
        return t

    def is_busted(self):
        t = self.total
        self.total = t > 21
        return self.total

    
class BJ_Player(BJ_Hand):
    """Gracz w BlackJack"""
    def is_hitting(self):
        response = gry.aks_yes_no("\n" + self.name + ", chcesz dobrać kartę? (T/N): ")
        return response == "t"

    def bust(self):
        print(self.name, "ma furę")
        self.lose()

    def lose(self):
        print(self.name, "przegrywa")

    def win(self):
        print(self.name, "wygrywa")

    def push(self):
        print(self.name, "remisuje")

    
class BJ_Dealer(BJ_Hand):
    """Rozdający w BlackJack"""
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "ma furę")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

    
class BJ_Game(object):
    """Gra w BlacJacka"""
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Rozdający")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        """Rozdaj każdemu graczowi po dwie karty"""
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card() #ukryj pierwszą kartę rozdającego
        for player in self.players:
            print(player)
        print(self.dealer)

        #rozdaj graczom dodatkowe karty
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card() #odsłoń pierwszą kartę rozdającego

        if not self.still_playing:
            """Poniewaz wszyscy gracze dostali furę pokaż rękę rozdającego"""
            print(self.dealer)
        else:
            """daj dodatkowe karty rozdającemu"""
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                """wygrywa każdy kto pozostaje w grze"""
                for player in self.still_playing:
                    player.win()
            else:
                """Porównaj puknkty każego gracza ppozostająceo w gze z punktami"""
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

            #usun karty wszystkich graczy
            for player in self.players:
                player.clear
            self.dealer.clear()
            
                                    
            
def main():
    print("\t\tWitaj w grze 'Blackjack'!\n")

    names = []
    number = gry.Player.ask_number("Podaj liczbę graczy (1 - 7): ", low = 1, high = 8)

    for i in range(number):
        name = input("Wprowadź nazwę gracza: ")
        names.append(name)
    print()

    game = BJ_Game(names)

    again = None

    while again != "n":
        game.play()
        again = gry.ask_yes_no("\nCzy chcesz zagrać ponownie?: ")
        
main()
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
        













































    
