def plot_szyfruj(slowo: str, klucz: int=3):
    """Funkcja przyjmuje słowo i zwraca je zaszyfrowanie według klucza, domyślnie wartości 3"""
    dl_slowa = len(slowo)
    lista_znakow = [["~" for i in range(klucz)] for j in range(dl_slowa)]
    kolumny = [i for i in range(klucz)]
    szyfr = ""

    # aby uzyskać "płotek", dodajemy kolumny odliczane do 1
    for i in range(klucz-2, 0, -1):
        kolumny.append(i)

    wiersz = 0
    while slowo:
        for i in kolumny:
            if slowo:
                # przepisujemy pierwszy znak z jawnego tekstu
                lista_znakow[wiersz][i] = slowo[0]
                # przepisujemy wszystkie elementy bez pierwszego znaku do slowo
                slowo = slowo[1:]
                wiersz += 1

    # łączymy znaki , jeśli są różne od "~"
    for i in range(klucz):
        for j in range(len(lista_znakow)):
            if lista_znakow[j][i] != "~":
                szyfr += lista_znakow[j][i]

    return szyfr

def plot_odszyfruj(szyfr: str, klucz: int=3):
    """Odszyfrowywuje słowo, klucz domyślnie ma wartość 3"""
    kopia = szyfr[:]   # Użyjemy kopii do wypełnienia listy
    dl_szyfru = len(szyfr)    # Kopia długości szyfru
    odszyfrowane = ""    # Odszyfrowane słowo
    szyfrowane_znaki = [["~" for i in range(dl_szyfru)] for j in range(klucz)]    # Lista na słowo

    # Wypełniamy listę * w miejscach liter
    kolumna = 0
    wiersz = [i for i in range(klucz)]
    for i in range(klucz-2, 0, -1):
        wiersz.append(i)

    while kopia:
        for i in wiersz:
            if kolumna < dl_szyfru:
                szyfrowane_znaki[i][kolumna] = "*"
                kolumna += 1
                kopia = kopia[1:]

    # Uzupełnij listę literami
    for i in range(klucz):
        for j in range(dl_szyfru):
            if szyfrowane_znaki[i][j] == "*":
                szyfrowane_znaki[i][j] = szyfr[0]
                szyfr = szyfr[1:]

    # Uzupełniaj słowo idąc po kolumnach
    for i in range(dl_szyfru):
        for j in range(klucz):
            if szyfrowane_znaki[j][i] != "~":
                odszyfrowane += szyfrowane_znaki[j][i]

    return odszyfrowane

if __name__ == "__main__":
    print("Ten plik nie powinien być wykonywany samodzielnie.")
