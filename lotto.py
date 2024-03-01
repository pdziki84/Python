#Program losuje 6 z 49 niepowtarzajacych się liczb

import random

lista = []

random.seed()

while(len(lista) < 6):
    i = random.randint(1,49)
    if(i in lista):
        continue
    else:
        lista.append(i)

lista.sort()
print(lista)

