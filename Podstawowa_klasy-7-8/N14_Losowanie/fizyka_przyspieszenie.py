def obliczenie():
    from random import random
    v_pocztkowe = random() * 10
    v_koncowe = random() * 100
    czas = random() * 20

    return (v_koncowe - v_pocztkowe) / czas

# wykonujemy funkcję
print(obliczenie())
print(obliczenie())
print(obliczenie())

# wersja z zaokrągleniem
print(round(obliczenie(),2))
print(round(obliczenie(),2))
print(round(obliczenie(),2))

"""
# przykład wykonania
4.048711976235929
24.8489002527046
2.011837140557314
#
# wersja z zaokrągleniem
31.21
3.62
4.33

"""
