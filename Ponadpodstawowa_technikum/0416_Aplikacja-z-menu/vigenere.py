def vig_tworzenie_klucza(tekst_jawny: str, slowo_klucz: str):
    from itertools import cycle
    klucz = ""
    pary = zip(tekst_jawny, cycle(slowo_klucz))
    for para in pary:
        klucz += para[1].upper()
    return klucz

def vig_szyfruj(napis: str, slowo_klucz: str):
    klucz = vig_tworzenie_klucza(napis, slowo_klucz)
    szyfrogram = ""
    for poz, litera in enumerate(napis.upper()):
        x = 65 + ((ord(litera) + ord(klucz[poz])) % 26 )
        szyfrogram += chr(x)
    return szyfrogram

def vig_odszyfruj(szyfr: str, klucz: str):
    tekst_jawny = ""
    for poz, litera in enumerate(szyfr.upper()):
        x = 65 + ((ord(litera) - ord(klucz[poz]) + 26) % 26 )
        tekst_jawny += chr(x)
    return tekst_jawny

if __name__ == "__main__":
    print("Ten plik nie powinien być wykonywany samodzielnie.")
