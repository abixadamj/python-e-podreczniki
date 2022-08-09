# plik zawierający dodatkowe funkcje
import sys


def pomoc(app_main: object):
    # Funkcja wyświetlająca pomoc w trybie nieinteraktywnym

    tekst = f"""
Pomoc dla programu: {app_main.app_name}
===============================================================
Zakładamy możliwości wykonania:
$ python3 app_glowna.py --help    -> wyświetli ten tekst

$ python3 app_glowna.py <szyfr> <tekst> <opcje_dla_szyfru>

<szyfr> - możliwe opcje to {app_main.rodzaje_szyfrowania} - określa rodzaj szyfrowania
<tekst> - tekst jawny do zaszyfrowania
<opcje_dla_szyfru> - ewentualne opcje dla szyfrowania:
  - cezar = liczba całkowita określająca przesunięcie w alfabecie
  - plf = ciąg znaków określający klucz do budowania tablicy
  - vig = ciąg znaków określający klucz do budowania klucza
  - plot = liczba całkowita określająca wysokość płotka

Przykłady wywołania:

$ python3 app_glowna.py cezar LinuxToSystemOperacyjny 15
Szyfrogram: AxcjmIdHnhitbDetgprnycn

$ python3 app_glowna.py plf LinuxToSystemOperacyjny OPENSOURCE
Szyfrogram: ('GTAOLZPONZSLNJENCBXAOMZY', ['O', 'P', 'E', 'N', 'S', 'U', 'R', 'C', 'A', 'B', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'T', 'V', 'W', 'X', 'Y', 'Z'])
"""
    print(tekst)
    sys.exit(0)


def zapis_dziennika(logging: object, info: str):
    from datetime import datetime

    czas = datetime.now()
    log = f"({czas}) - {info}"
    logging.info(log)
