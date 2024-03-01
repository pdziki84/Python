# Ten program wlicczy odsetki



spk = float(input("Podaj stan początkowy konta: "))
p = float(input("Podaj stope oprocentowania: "))
n = int(input("Podaj okres w latach jaki ma być policzony: "))

p_temp = p / 100
n_temp = n * 12
suma = spk

for i in range(n_temp):
    suma = suma + (p_temp * suma)/12
    print(round(suma, 2))


print("Kapitał po", n_temp, "miesiącach będzie wynosił: ", round(suma, 2))


#to liczy ale z kapitalizacją roczną, trzeba zrobić pętlę która będzie zliczała po miesiącu

#suma = spk + (p * spk) * n_temp
