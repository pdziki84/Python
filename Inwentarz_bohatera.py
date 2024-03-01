#Inwentarz bohatera
#Demonstracja tworzenia krotki

#utwórz pustą krrotkę
inventory = ()

#potraktuj krotkę jako warunek
if not inventory:
    print("Nie posiadasz niczego")

input("\nAby kontynuować misję nacisnij Enter.")

#utwórz krotkę zawierającą pewne elementy

inventory = ("miecz",
             "tarcza",
             "zbroja",
             "napój uzdrawiający")

#wyświetl krotkę
print("wykaz zawartości krotki: ")
print(inventory)

#Wyświetl każdy element krotki
print("\nEleenty twojego wyposażenia: ")
for item in inventory:
    print(item)

# Dokonaj konkatenacji krotek
chest = ("złoto","klejnoty")

print("Znajdujesz skrzynie któa zwiera: ")
print(chest)
print("Dodajesz zawartość skrzynie do swojego inwentarza.")
inventory += chest
print("Twój aktualny inwentarz to: ")
print(inventory)

input("\nAby zakończyć program, wciśnij Enter")
