def plf_sekretna_tablica(klucz: str):

    # dla tablicy 5x5 używamy alfabetu bez zanku "Q"
    alphabet = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
    tablica = []

    # kopiujemy znaki, ignorujemy duplikaty
    for znak in klucz.upper():
        if znak not in tablica and znak in alphabet:
            tablica.append(znak)

    # wypełniamy pozostałe znaki w tablicy
    for znak in alphabet:
        if znak not in tablica:
            tablica.append(znak)

    return tablica

def plf_zwroc_pary(tekst_jawny: str):
    from itertools import islice
    # sprawdzamy długość tekstu
    if len(tekst_jawny)%2 == 1:
        tekst_jawny += "x"
    # tworzymy iterator z tekstu w postaci wielkich liter
    iterator = iter(tekst_jawny.upper())
    # zwracamy za pomocą yield kolejne elementy
    while True:
       para_znakow = tuple(islice(iterator, 2))
       if not para_znakow:
           return
       yield para_znakow

def plf_znajdz_szyfr_pary(tablica: list, para_znakow: tuple):
    znak_1, znak_2 = para_znakow
    wiersz_1, kolumna_1 = divmod(tablica.index(znak_1), 5)
    wiersz_2, kolumna_2 = divmod(tablica.index(znak_2), 5)

    if wiersz_1 == wiersz_2:
        tekst = tablica[wiersz_1*5+(kolumna_1+1)%5]
        tekst += tablica[wiersz_2*5+(kolumna_2+1)%5]
    elif kolumna_1 == kolumna_2:
        tekst = tablica[((wiersz_1+1)%5)*5+kolumna_1]
        tekst += tablica[((wiersz_2+1)%5)*5+kolumna_2]
    else:
        tekst = tablica[wiersz_2*5+kolumna_1]
        tekst += tablica[wiersz_1*5+kolumna_2]
    return tekst

def plf_odszyfruj_pare(tablica: list, para_znakow: tuple):
    znak_1, znak_2 = para_znakow
    wiersz_1, kolumna_1 = divmod(tablica.index(znak_1), 5)
    wiersz_2, kolumna_2 = divmod(tablica.index(znak_2), 5)

    if wiersz_1 == wiersz_2:
        tekst = tablica[wiersz_1*5+(kolumna_1-1)%5]
        tekst += tablica[wiersz_2*5+(kolumna_2-1)%5]
    elif kolumna_1 == kolumna_2:
        tekst = tablica[((wiersz_1-1)%5)*5+kolumna_1]
        tekst += tablica[((wiersz_2-1)%5)*5+kolumna_2]
    else:
        tekst = tablica[wiersz_2*5+kolumna_1]
        tekst += tablica[wiersz_1*5+kolumna_2]
    return tekst

def plf_szyfruj(tekst_jawny: str, klucz: str):
    # tworzymy tablicę szyfrowania
    tablica = plf_sekretna_tablica(klucz)
    # przetwarzamy tekst jawny na szyfrogram
    szyfrogram = ""
    for para in plf_zwroc_pary(tekst_jawny):
        szyfrogram += plf_znajdz_szyfr_pary(tablica, para)
    # zwracamy szyfr oraz tablicę
    return (szyfrogram, tablica)

def plf_odszyfruj(szyfr: tuple):
    tekst_jawny = ""
    szyfrogram = szyfr[0]
    tablica = szyfr[1]
    for para in zwroc_pary(szyfrogram):
        tekst_jawny += plf_odszyfruj_pare(tablica, para)
    return tekst_jawny

if __name__ == "__main__":
    print("Ten plik nie powinien być wykonywany samodzielnie.")
