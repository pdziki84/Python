#Prograam liczy wartości trygonometryczne podanego kata

import math

kat = float(input("Podaj wartość kąta do przeliczenia: "))

sinus = math.sin(kat)
cosinus = math.cos(kat)
tangens = math.tan(kat)
cotangens = 1 / tangens


print("sinus kąta %.2f wynosi %f" % (kat, sinus))
print("cosinus kąta %.2f wynosi %f" % (kat, cosinus))
print("tangens kąta %.2f wynosi %f" % (kat, tangens))
print("cotangens kąta %.2f wynosi %f" % (kat, cotangens))
