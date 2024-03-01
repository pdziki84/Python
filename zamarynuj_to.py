#Zamarynuj to
#Demonstruje marynowanie i odkładanie danych na półkę


def marynowanie():
    import pickle, shelve

    print("Marynowani list")

    variety = ["łagodny","pikantny","kwaszony"]
    shape = ["cały","krojony wzdłóż","w plasterkach"]
    brand = ["Dawtona","Klimex","Vortumnus"]

    f = open("pikle1.dat", "wb")

    pickle.dump(variety, f)
    pickle.dump(shape, f)
    pickle.dump(brand, f)

    f.close()

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")




def odmarynowanie():
    import pickle, shelve
    print("\nOdmarynowanie list.")
    f = open("pikle1.dat", "rb")
    variety = pickle.load(f)
    shape = pickle.load(f)
    brand = pickle.load(f)
    
    
    print(variety)
    print(shape)
    print(brand)

    f.close()
    
    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

def polkwanie():
    import pickle, shelve
    print("\nOdladanie list na polke")
    s = shelve.open("pikle2.dat")

    s["odmiana"] = ["łagodny","pikantny","kwaszony"]
    s["ksztalt"] = ["cały","krojony wzdłóż","w plasterkach"]
    s["marka"] = ["Dawtona","Klimex","Vortumnus"]

    s.sync()



    print("\nPobieranie list z pliku półki: ")
    print("marka - ", s["marka"])
    print("kształt - ", s["ksztalt"])
    print("odmiana - ", s["odmiana"])

    s.close()

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")







    

#marynowanie()
#odmarynowanie()
polkwanie()
