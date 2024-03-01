#funkcja oblicza średnia dla dowolnej liczby argumentów
def avg(*arg):
    if(len(arg) == 0):
        return 0
    else:
        s = 0
        l = len(arg)
        for x in arg:
            s += x
        return s/l


avg(5)
