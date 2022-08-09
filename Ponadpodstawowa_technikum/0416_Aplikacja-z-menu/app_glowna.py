# importy standardowych modułów - one powinny być dostępne zawsze
import sys
import logging

# próba importu modułów zawierających funkcje dodatkowe i szyfrujące
try:
    from app_funkcje import *
    from cezara import *
    from playfair import *
    from plotkowy import *
    from vigenere import *
except:
    # informacja dla użytkownika, jeśli wystąpił jakiś błąd
    print("Problem przy imporcie modułów dodatkowych - sprawdź ich istnienie.")
    # oraz zakończenie działania aplikacji
    sys.exit(0)

# zdefiniowanie pliku dziennika aplikacji i jego minimalnej konfiguracji
logging.basicConfig(filename="app_dziennik.log", filemode="a", level=logging.INFO)

# próba importu zewnętrznych modułów
try:
    import PySimpleGUI as sg
except:
    # informacja dla użytkownika, jeśli moduł nie jest zainstalowany
    print("Brak modułu PySimpleGUI - dodaj go narzędziem pip")
    # oraz zakończenie działania aplikacji
    sys.exit(0)


# zdefiniowanie pustej klasy dla celów przetrzymywania krytycznych informacji
class APP:
    pass

# oraz instancji tej klasy
app_main = APP()

# przypisujemy pewne właściwości
app_main.app_name = "Aplikacja szyfrująca"
app_main.rodzaje_szyfrowania = ["cezar", "plf", "vig", "plot"]

# sprawdzamy, czy aplikacja została wywołana z jakimkolwiek parametrem, wówczas ustawiamy właściwość trybu pracy
if len(sys.argv) > 1:
    app_main.tryb_pracy = "script"
else:
    app_main.tryb_pracy = "gui"


# teraz część odpowiedzialna za działanie nieinteraktywne
if app_main.tryb_pracy == "script":
    # spradzenie, czy nie trzeba pomocy...
    opcja_1 = sys.argv[1]
    if (opcja_1 == "--help"
        or not opcja_1 in app_main.rodzaje_szyfrowania
        ):
        pomoc(app_main)
    else:
        if opcja_1 == "cezar":
            szyfrogram = cezar_szyfruj(sys.argv[2], int(sys.argv[3]))
        if opcja_1 == "plf":
            szyfrogram = plf_szyfruj(sys.argv[2], sys.argv[3])
        if opcja_1 == "vig":
            szyfrogram = vig_szyfruj(sys.argv[2], sys.argv[3])
        if opcja_1 == "plot":
            szyfrogram = plot_szyfruj(sys.argv[2], int(sys.argv[3]))
        # na końcu zapisujemy dziennik i wyświetlamy na ekranie
        zapis_dziennika(logging, f"Szyfrowanie: {opcja_1} | {sys.argv[2]} -> {szyfrogram} ")
        print(f"Szyfrogram: {szyfrogram}")
    # zakończenie działania programu
    logging.shutdown()
    sys.exit(0)


# teraz część odpowiedzialna za działanie interaktywne (graficzny interfejs)
if app_main.tryb_pracy == "gui":
    # definiujemy elementy menu:
    menu_def = [["Menu główne", ["Szyfr Cezara", "Szyfr Playfair", "Szyfr Vigenere'a", "Szyfr Płotkowy"  ]],
                 ["Informacje", ["O programie", "Koniec pracy"]],
                 ]

    layout = [
            [sg.Menu(menu_def, )],
            [sg.Text("Program: " + app_main.app_name)],
             ]

    window = sg.Window(app_main.app_name, layout, auto_size_text=False)

    # tworzymy odpowiednie definicje okien
    layout_cez_plot = [
            [sg.Text("Podaj tekst jawny (max. 35 znaków)")],
            [sg.Input(key="dane")],
            [sg.Text("Opcja: przesunięcie/płotek"), sg.Input(size=(3, 1), key="k")],
            [sg.Text("Tekst wynikowy: ")],
            [sg.Text(" " * 40, size=(40,1), auto_size_text=True, key="-OUT-")],
            [sg.Button('Wykonaj'), sg.Exit()]]

    layout_plf_vin = [
            [sg.Text("Podaj tekst jawny (max. 35 znaków)")],
            [sg.Input(key="dane")],
            [sg.Text("Podaj klucz do tworzenia tablicy (max. 35 znaków)")],
            [sg.Input(key="klucz")],
            [sg.Text(" " * 40, size=(40,1), auto_size_text=True, key="-OUT-")],
            [sg.Button('Wykonaj'), sg.Exit()]]
    # aby móc modyfikować elementy okna, musimy tworzyć okna z parametrem finalize=True
    # oraz ukryć okno na początku działania programu
    # więcej informacji [w zgłoszeniach biblioteki](https://github.com/PySimpleGUI/PySimpleGUI/issues/1276) oraz [w dokumentacji biblioeki](https://pysimplegui.readthedocs.io/en/latest/cookbook/#persistent-window-with-text-element-updates)
    okno_cez_plot = sg.Window("Szyfrowanie", layout_cez_plot, finalize=True)
    okno_plf_vig = sg.Window("Szyfrowanie", layout_plf_vin, finalize=True)
    # ukrywamy widoczność okien
    okno_cez_plot.Hide()
    okno_plf_vig.Hide()

    # główna pętla programu
    while True:
        event, values = window.read()
        if event == "O programie":
            sg.popup("O programie", 'Wersja 1.0', 'Szyfrowanie w PySimpleGUI...')

        # w zależności od rodzaju szyfrowania wyświetlamy odpowiednie okna
        if event == "Szyfr Cezara" or event == "Szyfr Płotkowy":
            okno_cez_plot.UnHide()
            while True:
                # wyświetlamy okno o odpowiedniej nazwie
                okno_cez_plot.TKroot.title(event)
                dzialaj, wartosci = okno_cez_plot.read()
                if dzialaj == "Wykonaj":
                    # staramy się odczytać dane
                    try:
                        klucz = int(wartosci["k"])
                        tekst_jawny = wartosci["dane"]
                    # w przypadku niepowodzenia przyjmujemy wartości domyślne
                    except:
                        klucz = 3
                        tekst_jawny = "TEKST"

                    # wykonujemy fyzyczne szyfrowanie
                    if event == "Szyfr Cezara":
                        szyfrogram = cezar_szyfruj(tekst_jawny, klucz)
                    else:
                        szyfrogram = plot_szyfruj(tekst_jawny, klucz)
                    # aktualizujemy wynikowy szyfrogram
                    okno_cez_plot["-OUT-"].update(szyfrogram)
                    # zapisujemy dziennik
                    zapis_dziennika(logging, f"Szyfrowanie: {event} | {tekst_jawny} -> {szyfrogram} ")
                else:
                    # ukrywamy okno i wracamy do głównej pętli
                    okno_cez_plot.Hide()
                    break

        if event == "Szyfr Playfair" or event == "Szyfr Vigenere'a":
            okno_plf_vig.UnHide()
            while True:
                # wyświetlamy okno o odpowiedniej nazwie
                okno_plf_vig.TKroot.title(event)
                dzialaj, wartosci = okno_plf_vig.read()
                if dzialaj == "Wykonaj":
                    # staramy się odczytać dane
                    try:
                        tekst_jawny = wartosci["dane"]
                        klucz_txt = wartosci["klucz"]
                    # w przypadku niepowodzenia przyjmujemy wartości domyślne
                    except:
                        klucz_txt = "KLUCZ"
                        tekst_jawny = "TEKST"

                    # wykonujemy fyzyczne szyfrowanie
                    if event == "Szyfr Playfair":
                        szyfrogram = plf_szyfruj(tekst_jawny, klucz_txt)
                        wynik = szyfrogram[0]
                    else:
                        szyfrogram = vig_szyfruj(tekst_jawny, klucz_txt)
                        wynik = szyfrogram
                    # aktualizujemy wynikowy szyfrogram
                    okno_plf_vig["-OUT-"].update(wynik)
                    # zapisujemy dziennik
                    zapis_dziennika(logging, f"Szyfrowanie: {event} | {tekst_jawny} -> {szyfrogram} ")
                else:
                    # ukrywamy okno i wracamy do głównej pętli
                    okno_plf_vig.Hide()
                    break

        if event == 'Koniec pracy' or event == None:
            wynik = sg.popup_yes_no("KONIEC", "Czy chcesz zakończyć?")
            if wynik.upper() == "YES":
                logging.shutdown()
                sys.exit(0)

# na wszelki wypadek na końcu programu zamykamy wszystko bezpiecznie
logging.shutdown()
sys.exit(0)
