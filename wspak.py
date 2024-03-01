# Program wyświetla poszczególne wyraz wspak


t = input("Wpisz dłuższy tekst >")

for w in t.split(): #dla każdego wyrazu w zdaniu
    l = list(w)     #tworzymy liste jego liter
    l.reverse()     #odrwacamy jej kolejnosc
    print(''.join(l), end = ' ')#łączymy ją w całość i wyświetlamy bez sepaatorów
    
