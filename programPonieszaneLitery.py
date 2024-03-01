# Wymieszane litery
# Komputer wybiera losowo słowo, a potem miesza w nim litery
# Gracz powinien odgadnąć pierwotne słowo

import random

WORDS = ("python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon")

#wybieram losowo jedno słowo

word = random.choice(WORDS)

correct = word

#utwórz pomieszaną wersje słowa

jumble = ""

while word:
    position = random.randrange(len(word))
    jumble+=word[position]
    word = word[:position] + word[(position + 1):]


#rozpocznij grę
print("""
            Witaj w grze 'Wymieszane litery'!
    Uporządkuj litery aby odtworzyć prawidłowe słowo
""")

print("Zgadnij, jakie to słowo", jumble)

guess= input("\nTwoja odpowiedz: ")
while(guess != correct and guess != ""):
    print("niestety to nie to słowo.")
    guess = input("Twoja odpowiedz: ")

    if(guess == correct):
        print("Gratulacje zgadłeś")

print("Dziękuję za udział w grze.")
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
