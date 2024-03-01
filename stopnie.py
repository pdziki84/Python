##Woda zamarza przy 32 stopniach Fahrenheita,
##a wrze przy 212 stopniach Fahrenheita.
##Napisz program „stopnie.py”,
##który wyświetli tabelę przeliczeń stopni Celsjusza na stopnie Fahrenheita
##w zakresie od –20 do +40 stopni Celsjusza (co 5 stopni).
##Pamiętaj o wyświetlaniu znaku plus/minus przy temperaturze


print("%4s%6s" % ("Celc.", "Fahr."))
for x in range(-20, 41, 5):
    print("%+3i%+8i" % (x, (x* 9/5) + 32))
