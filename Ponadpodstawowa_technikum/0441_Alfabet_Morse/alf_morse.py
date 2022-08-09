import pickle

def zapis_danych():
    alfabet_morse = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        ", ": "--..--",
        ".": ".-.-.-",
        "?": "..--..",
        "/": "-..-.",
        "-": "-....-",
        "(": "-.--.",
        ")": "-.--.-",
        "Ą": ".-.-",
        "Ć": "-.-..",
        "Ę": "..-..",
        "Ł": ".-..-",
        "Ń": "--.--",
        "Ó": "---.",
        "Ś": "...-...",
        "Ż": "--..-.",
        "Ź": "--..-",
        " ": chr(3),
    }

    with open("plik_danych.dat", "wb") as p:
        pickle.dump(alfabet_morse, p)


def odczyt_danych(plik="plik_danych.dat"):
    import os.path

    if not os.path.isfile(plik):
        return None

    with open(plik, "rb") as p:
        dane = pickle.load(p)
    return dane


def zakoduj(tekst_jawny="Python Linux", tablica_kodowania=None):

    start_of_text = chr(2)
    ack = chr(6)
    end_of_transmission = chr(4)

    zakodowany_tekst = ""
    zakodowany_tekst += start_of_text

    for litera in tekst_jawny.upper():
        try:
            zakodowany_tekst += tablica_kodowania[litera] + ack
        except KeyError:
            pass
    zakodowany_tekst += end_of_transmission

    return zakodowany_tekst


def odkoduj(tekst_zakodowany, tablica_kodowania):

    def odk_litera(kod, tablica_kodowania):
        for j,k in tablica_kodowania.items():
            if kod == k:
                return j
        else:
            return ""

    start_of_text = chr(2)
    ack = chr(6)
    end_of_transmission = chr(4)

    if (
        len(tekst_zakodowany) < 3
        or tekst_zakodowany[0] != start_of_text
        or tekst_zakodowany[-1] != end_of_transmission
    ):
        return False
    else:
        # pozbywamy się pierwszego i ostatniego znaku
        tekst = tekst_zakodowany[1:-1]
        # dzielimy na poszczególne słowa - separator ETX
        tekst_lista = tekst.split(tablica_kodowania[' '])
        dekodowany = ""
        for slowo in tekst_lista:
            # dzielimy na litery - separator ACK
            slowo = slowo.split(ack)
            for litera in slowo:
                # odszukujemy literę odpowiadającą kodowi morsea
                dekodowany += odk_litera(litera, tablica_kodowania)
            dekodowany += " "
        # uwaga! mały punkt problematyczny - ostatnie słowo ma dodatkową spację,
        # trzeba na końcu się jej pozbyć
        return dekodowany[:-1]


zapis_danych()
dane_wczytane = odczyt_danych()
# print(dane_wczytane)
kod = zakoduj(tablica_kodowania=dane_wczytane)
print(kod)
dekod = odkoduj(kod, dane_wczytane)
print(dekod)

# kolejna próba
kod = zakoduj("To jest szyfr @- (łódź) @- i koniec.", tablica_kodowania=dane_wczytane)
print(kod)
dekod = odkoduj(kod, dane_wczytane)
print(dekod)


kod = zakoduj("To jest tekst do zakodowania.", tablica_kodowania=dane_wczytane)
print(kod)
dekod = odkoduj(kod, dane_wczytane)
print(dekod)


# kolejna próba - False
kod = zakoduj("", tablica_kodowania=dane_wczytane)
print(kod)
dekod = odkoduj(kod, dane_wczytane)
print(dekod)

tekst = "Linux - swietny system operacyjny.".upper()
zak_wynik = zakoduj(tekst, tablica_kodowania=dane_wczytane)
dek_wynik = odkoduj(zak_wynik, dane_wczytane)
print(tekst,repr(tekst))
print(dek_wynik, repr(dek_wynik))
print(tekst == dek_wynik)

wynik = odkoduj("", tablica_kodowania=dane_wczytane)
print(wynik)
