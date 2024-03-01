# pierwszy program wielokrotnie rozgałęziony

print("Ten program porownuje dwie liczby")

print("Program przewidzi twoją długośc życia")


odp = input("Czy palisz papierosy?")

if(odp == "Tak" or odp == "TAK" or odp == "tak" or odp == 'no pewnie' ):
    odp = input("A czy się zaciągasz?")
    if(odp == "Tak" or odp == "TAK" or odp == "tak" or odp == 'no pewnie' ):
        print("Nie pożyjesz długo")
    else:
        print("To pożjesz długo")
else:
    print("To pożyjesz bardzo długo")
    
