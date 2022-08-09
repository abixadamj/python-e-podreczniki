# wczytujemy wszystkie funkcje modułu import
from turtle import *

# definiujemy funkcję - zapisujemy, co ma ona robić
# możemy ustalić różne parametry - czyli zmienne,
# które przy każdym wywołaniu
# mogą mieć różne wartości (argumenty)
def wielokat(dlugosc, ilosc):
    # blok kodu - wcięcie 4 spacje
    # najpierw sprawdzamy, czy ilosc jest odpowiednia
    if ilosc > 360:
        # jeśli warunek jest spełniony
        # kończymy działanie funkcji
        # i zwracamy wartość "False" (logiczny fałsz)
        return False

    # jeśli warunek nie jest spełniony, a więc ilosc <= 360
    kat = 360 / ilosc
    # teraz pętla - wykonujemy ilosc razy
    # zwracamy uwagę na kolejne wcięcie
    for x in range(ilosc):
        fd(dlugosc)
        lt(kat)

# tu wywołujemy funkcję - każemy jej wykonać to,
# co wcześniej zdefiniowaliśmy - nic się nie wykona,
# jeśli podamy zbyt dużą wartość dla ilosc
wielokat(150, 7)
wielokat(50, 380)
wielokat(70, 20)
