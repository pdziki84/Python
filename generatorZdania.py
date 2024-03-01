#funkcja generująca losowe zdanie o zadanej liczbnie wyrazów


def brednie(wyrazy = 5):
    from random import seed, randint

    seed()
    tekst = ""

    for wyraz in range(wyrazy):
        for litera in range(randint(1,10)):
            tekst += chr(randint(ord('a'), ord('z')))
        tekst +=" "
    return ((tekst[:-1]+".").capitalize())


brednie(5)
