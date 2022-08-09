def cezar_szyfruj(tekst: str, klucz: int=3):
    """domyślną wartością przesunięcia jest 3"""
    szyfr = ""
    for ch in tekst:
        nowy_kod = ord("~")
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            nowy_kod = ord(ch) + klucz
            if (nowy_kod > ord('z')):
                nowy_kod -= 26
        if ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
            nowy_kod = ord(ch) + klucz
            if (nowy_kod > ord('Z')):
                nowy_kod -= 26
        szyfr += chr(nowy_kod)
    return szyfr

def cezar_deszyfruj(tekst: str, klucz: int=3):
    """domyślną wartością przesunięcia jest 3"""
    odszyfrowany = ""
    for ch in tekst:
        nowy_kod = ord("~")
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            nowy_kod = ord(ch) - klucz
            if (nowy_kod < ord('a')):
                nowy_kod += 26
        if ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
            nowy_kod = ord(ch) - klucz
            if (nowy_kod < ord('A')):
                nowy_kod += 26
        odszyfrowany += chr(nowy_kod)
    return odszyfrowany

if __name__ == "__main__":
    print("Ten plik nie powinien być wykonywany samodzielnie.")
