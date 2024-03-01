#Lista ocen studentów

class Student:
    imie = ""
    nazwisko = ""
    ocena = 0.00

ilosc_studentow = 0
suma_ocen = 0
studenci = []
nr = 0
while True:
    naz = input("podaj nazwisko studenta nr %i (Enter = koniec): " %(nr + 1))
    if not naz:
        break
    studenci.append(Student())
    studenci[nr].nazwisko = naz
    studenci[nr].imie = input("Podaj imie studenta ne %i: " %(nr+1))
    studenci[nr].ocena = float(input("Podaj ocenę studenta ne %i: " %(nr+1)))
    ilosc_studentow  += 1
    suma_ocen += studenci[nr].ocena
    nr += 1

srednia = suma_ocen / ilosc_studentow    
print()
print("%-4s %-14s %-10s %7s" %("Lp.","Nazwisko","Imię", "Ocena"))
for s in studenci:
    print("%3i. %-14s %-10s %7.2f" %(studenci.index(s) + 1, s.nazwisko, s.imie, s.ocena))

print("Średnia wszystkich ocen: %.2f" %srednia)
