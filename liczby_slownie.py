def przelicz(n=""):
    w={"jeden":1, "dwa":2, "trzy":3, "cztery":4, "pięć":5, "sześć":6,
    "siedem":7, "osiem":8, "dziewięć":9, "dziesięć":10, "jedenaście":11,
    "dwanaście":12, "trzynaście":13, "czternaście":14, "piętnaście":15,
    "szesnaście":16, "siedemnaście":17, "osiemnaście":18,
    "dziewiętnaście":19, "dwadzieścia":20, "trzydzieści":30,
    "czterdzieści":40, "pięćdziesiąt":50}

    l = n.split()
    s = 0
    for x in l:
        if(x in l):
            s += w[x]
    return s

t = input("Wpisz liczbę 0d 1 do 59: ")
print("Wartość po przeliczeniu to: ", przelicz(t))

    
