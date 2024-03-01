##Zdefiniuj funkcję "geo", która dla podanych trzech parametrów:
##n=numer elementu ciągu, a1=wartość pierwszego elementu ciągu
##(domyślnie 1), q=wartość iloczynu ciągu geometrycznego
##(domyślnie 2) zwróci n-ty element ciągu geometrycznego.

def geo(n, a1 = 1, q = 2):
    import math
    
    an = a1 * math.pow(q, n-1)

    return an
    

geo()
