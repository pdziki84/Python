# pierwszy program rozgałęziony

print("Ten program porownuje dwie liczby")

x = input("Podaj pierwszą z dwóch liczzb: ")
y = input("Podaj drugą z dwóch liczzb: ")


if(x==y):
    temp = "taka sama"
elif(x > y):
    temp = "większa"
else:
    temp = "mniejsza"



print("Liczba", x, " w stosunku do liczby", y, "jest", temp)
