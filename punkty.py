# program wylicza odległość między dwoma punktami

from math import hypot

p1x = int(input("Podaj współrzędną poziomą pierwszego punktu > "))
p1y = int(input("Podaj współrzędną pionową pierwszego punktu > "))
p2x = int(input("Podaj współrzędną poziomą drugiego punktu > "))
p2y = int(input("Podaj współrzędną pionową drugiego punktu > "))

print("odległość midzy tymi punktami wynosi %.3f" %hypot(p1x - p2x, p1y-p2y))


      
