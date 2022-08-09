# wczytujemy wszystkie funkcje modułu import
from turtle import *

# definiujemy funkcję - zapisujemy, co ma ona robić
# możemy ustalić różne parametry - czyli zmienne,
# które przy każdym wywołaniu
# mogą mieć różne wartości (argumenty)
def wielokat(dlugosc, ilosc):
    # blok kodu - wcięcie 4 spacje
    kat = 360 / ilosc
    fd(dlugosc)
    lt(kat)

# tu wywołujemy funkcję - każemy jej wykonać to,
# co wcześniej zdefiniowaliśmy
wielokat(150, 7)
# możemy wywołać funkcję kilka razy, podając różne argumenty
wielokat(10, 8)
wielokat(100, 5)
