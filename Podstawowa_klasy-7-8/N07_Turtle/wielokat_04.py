# wczytujemy wszystkie funkcje modułu import
from turtle import *
# wczytamy tez funckje z moduły random
from random import randint, choice

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

    # ustalamy możliwe kolory
    kolory = ["red", "green", "blue", "yellow", "purple", "brown"]

    # ustalamy grubość pisaka - losowa wartość 20 ~ 50 pixeli
    grubosc = randint(20, 50)
    pensize(grubosc)

    # teraz pętla - wykonujemy ilosc razy
    # zwracamy uwagę na kolejne wcięcie
    for x in range(ilosc):
        # przy każdym wykonaniu ustawiamy losowy kolor z listy
        jeden_kolor = choice(kolory)
        pencolor(jeden_kolor)
        # i dopiero teraz rysujemy
        fd(dlugosc)
        lt(kat)

# tu wywołujemy funkcję - każemy jej wykonać to,
# co wcześniej zdefiniowaliśmy - nic się nie wykona,
# jeśli podamy zbyt dużą wartość dla ilosc
wielokat(120, 9)
wielokat(50, 7)
wielokat(50, 380)
wielokat(70, 10)
