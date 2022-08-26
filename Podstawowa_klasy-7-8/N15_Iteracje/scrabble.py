def wartosc_znaku(znak):
    if znak in "ęóąśłżźćń":
        return 5
    elif znak in "eyuioa":
        return 2
    else:
        return 1


def licz_scrabble(slowo):
    wartosc_pkt = 0
    ilosc_znakow = 0
    for znak in slowo:
        ilosc_znakow += 1
        if znak == " ":
            print("Dwa słowa - dyskwalifikacja - wynik 0.")
            return 0
        wartosc_pkt += wartosc_znaku(znak)

    if ilosc_znakow > 10:
        wartosc_pkt += 10

    if ilosc_znakow > 15:
        wartosc_pkt += 20

    print(f"Słowo {slowo} uzyskuje {wartosc_pkt} pkt.")
    return wartosc_pkt


licz_scrabble("apartamentowiec")
licz_scrabble("żaba")

