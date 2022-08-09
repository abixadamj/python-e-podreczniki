import curses

def start():
    okno = curses.initscr()
    # sprawdzamy wymiary okna - min. 60 kolumn x 15 wierszy
    y, x = okno.getmaxyx()
    if y < 15 or x < 60:
        print("Niestety, okno jest zbyt małe.")
        print("Naciśnij dowolny klawisz...")
        klawisz = okno.getkey()
        koniec_gry(okno)
    # ustawiamy wartości operacyjne
    curses.noecho()  # nie wyświetlamy na ekranie bez potrzeby
    curses.cbreak()  # po naciśnięciu klawisza nie oczekujemy Entera dla potwierdzenia
    return okno


def koniec_gry(okno):
    from sys import exit

    curses.nocbreak()
    okno.keypad(False)
    curses.echo()
    curses.endwin()
    exit()


def napis_poczatkowy(okno):
    """
    Uwaga - współrzędne podajemy w posiaci (y,x)
    """
    okno.addstr(1, 1, "____              ___                         ___")
    okno.addstr(2, 1, "`Mb(      db      )d' 68b         68b         `MM")
    okno.addstr(3, 1, " YM.     ,PM.     ,P  Y89         Y89          MM")
    okno.addstr(
        4, 1, " `Mb     d'Mb     d'  ___   ____  ___   ____   MM   ____     ____"
    )
    okno.addstr(
        5, 1, "  YM.   ,P YM.   ,P   `MM  6MMMMb\`MM  6MMMMb  MM  6MMMMb   6MMMMb."
    )
    okno.addstr(
        6, 1, "  `Mb   d' `Mb   d'    MM MM'    ` MM 6M'  `Mb MM 6M'  `Mb 6M'   Mb"
    )
    okno.addstr(
        7, 1, "   YM. ,P   YM. ,P     MM YM.      MM MM    MM MM MM    MM MM    `'"
    )
    okno.addstr(8, 1, "   `Mb d'   `Mb d'     MM  YMMMMb  MM MMMMMMMM MM MMMMMMMM MM")
    okno.addstr(9, 1, "    YM,P     YM,P      MM      `Mb MM MM       MM MM       MM")
    okno.addstr(
        10, 1, "    `MM'     `MM'      MM L    ,MM MM YM    d9 MM YM    d9 YM.   d9"
    )
    okno.addstr(
        11, 1, "     YP       YP      _MM_MYMMMM9 _MM_ YMMMM9 _MM_ YMMMM9   YMMMM9"
    )
    okno.addstr(13, 3, "Wisielec - zgaduj litery, dobra litera nie odbiera prób.")
    okno.addstr(
        15,
        3,
        "Wisielec - naciśnij klawisz [SPACJA] aby rozpocząć grę...",
        curses.A_BOLD,
    )
    klawisz = okno.getkey()
    if klawisz != " ":
        koniec_gry(okno)
    else:
        okno.clear()


def losuj_slowo():
    from random import choice

    slowa = [
        "wisielec",
        "komputer",
        "Python",
        "Linux",
        "Windows",
        "informatyka",
        "programowanie",
    ]
    slowo = choice(slowa)
    return slowo


def wyglad_slowa(slowo, litery):
    dl = len(slowo)
    oddany_napis = "Odgadnięte słowo: "

    if litery == "":
        return "Odgadnięte słowo: " + "_ " * dl

    for litera in slowo:
        if litera in litery:
            oddany_napis += litera + " "
        else:
            oddany_napis += "_ "

    return oddany_napis


def stworz_wisielca():
    w = ["", "", "", "", "", "", "", "", "", "", "", ""]
    w[0] = "    _"
    w[1] = "   ( )"
    w[2] = "    -"
    w[3] = "    |"
    w[4] = "  / | \\"
    w[5] = " /  |  \\"
    w[6] = "    |"
    w[7] = "    |"
    w[8] = "    |"
    w[9] = "   / \\"
    w[10] = "  /   \\"
    w[11] = " /     \\"
    return w


def rysuj_wisielca(okno, wisielec, numer):
    okno.addstr(7 + numer, 60, wisielec[numer])


# główna aplikacja


okno = start()
okno.timeout(-1)  # oczekiwanie w nieskonczoność na naciśnięcie klawisza
napis_poczatkowy(okno)
szukane_slowo = losuj_slowo()
dl = len(szukane_slowo)
wykorzystano = 0
do_wykorzystania = 12  # maksimum długości wisielca
litery_odgadniete = ""
bledne = 0
poprawne = 0
odgadniete_slowo = wyglad_slowa(szukane_slowo, "")
wisielec = stworz_wisielca()


okno.addstr(3, 3, "Wisielec - szukamy słowa: " + "*" * dl, curses.A_BOLD)
okno.addstr(5, 3, "Teraz naciskaj kolejne litery.")
okno.addstr(6, 45, "Tutaj będzie wisielec:")
okno.addstr(7, 3, "Pozostało możliwych prób: ")
okno.addstr(8, 3, "Litery wykorzystane: ")
okno.addstr(9, 3, odgadniete_slowo)


while do_wykorzystania:
    napis_do_wykorzystania = str(do_wykorzystania).rjust(3, " ")
    okno.addstr(7, 30, napis_do_wykorzystania, curses.A_REVERSE)
    okno.move(8, 24 + wykorzystano + 1)
    klawisz = okno.getkey()

    if klawisz in szukane_slowo:
        if klawisz not in litery_odgadniete:
            wykorzystano += 1
            litery_odgadniete += klawisz
            okno.addch(8, 24 + wykorzystano, klawisz, curses.A_UNDERLINE)
            okno.addstr(9, 3, wyglad_slowa(szukane_slowo, litery_odgadniete))
            poprawne += szukane_slowo.count(klawisz)
            if poprawne == dl:
                okno.addstr(15, 10, "SUPER - GRATULACJE !!!!", curses.A_BLINK)
                okno.addstr(16, 15, "WYGRANA !!!!", curses.A_BLINK)
                okno.addstr(17, 8, "Naciśnij dowolny klawisz...", curses.A_BLINK)
                okno.refresh()
                klawisz = okno.getkey()
                koniec_gry(okno)
    else:
        wykorzystano += 1
        do_wykorzystania -= 1
        okno.addch(8, 24 + wykorzystano, klawisz)
        rysuj_wisielca(okno, wisielec, bledne)
        bledne += 1

    okno.refresh()

# teraz kod wykonany po pętli
okno.addstr(15, 10, "Przegrana !!!!", curses.A_BLINK)
okno.addstr(17, 8, "Naciśnij dowolny klawisz...", curses.A_BLINK)
okno.refresh()
klawisz = okno.getkey()
koniec_gry(okno)
