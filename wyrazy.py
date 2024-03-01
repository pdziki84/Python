#Program dzieli tekst na zdania

sentence = input("Wprowadź tekst do podziału na zdania: ")

#sentence = 'Każdy symbol w programach to także komórka w pamięci, której zawartość wpływa na działanie systemu. Możemy więc mówić, że symbol ma pewne znaczenie (wpływ na system). Czy jednak także coś oznacza – albo inaczej, czy się do czegoś odnosi? A może w systemie komputerowym te odniesienia są jedynie innym sposobem opisu tego, jak zmienna/symbol wpływa na system – czyli jakie ma znaczenie w systemie? Jeśli chodzi o odniesienia do rzeczywistości (co oznacza symbol poza wirtualnym światem komputerów) – to one w samych obliczeniach nie są ważne. Odniesienia te są symbolom nadawane poprzez urządzenia peryferyjne w komputerze, albo człowieka, interpretującego wyniki działania programów.'

zdania = sentence.split('.')




for zdanie in zdania:
    ilosc_wyrazow = zdanie.split()
    print(len(ilosc_wyrazow))
