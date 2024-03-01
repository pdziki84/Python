##Kalkulator BMI: Napisz program, który obliczy wskaźnik masy ciała (BMI)
##na podstawie wprowadzonych przez użytkownika danych (waga i wzrost).


def pobierz_dane():

    while True:
        try:
            wzrost = float(input("Podaj swój wzrost w metrach: "))
            if(wzrost <= 0):
                raise ValueError("Wzrost musi być liczbą dodatnią.")
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            waga = int(input("Podaj swoją wage w kilogramach: "))
            if(waga <= 0):
                raise("Waga musi być liczbą dodatnią")
            break
        except ValueError as e:
            print(e)
    return wzrost,waga

def oblicz_BMI(wzrost, waga):
    import math
    BMI = round((waga / math.pow(wzrost,2)),2)
    return BMI

def wyswietl_wyniki(BMI):
    komunikaty_BMI = {
        (0, 16):"WYGŁODZENIE",
        (16, 17):"WYCHUDZENIE",
        (17, 18.5):"NIEDOWAGE",
        (18.5, 24.9):"PRAWIDŁOWĄ MASĘ CIAŁA",
        (24.9, 29.9):"NADWAGĘ",
        (29.9, 34.9):"OTYŁOŚĆ I STOPNIA",
        (34.9, 39.9):"OTYŁOŚĆ II STOPNIA",
        (40.0, float('inf')): "OTYŁOŚĆ III STOPNIA"
        }


    for key, value in komunikaty_BMI.items():
        if key[0] <= BMI < key[1]:
            print("Twój BMI wynosi %.2f i wskazuje na %s" % (BMI, value))
            break


def kalkulator_BMI():
    wzrost, waga = pobierz_dane()
    BMI = oblicz_BMI(wzrost, waga)
    wyswietl_wyniki(BMI)
    

kalkulator_BMI()
    
