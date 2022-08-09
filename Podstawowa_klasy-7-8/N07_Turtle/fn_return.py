def funkcja_oblicza(parametr):
    # wewnątrz liczymy coś, np.
    wynik = (parametr + 5) * 3

    # tak obliczony wynik zwracamy
    return wynik


liczba = funkcja_oblicza(2)
print(liczba)
# wynikiem będzie 21


liczba = funkcja_oblicza(4)
print(liczba)
# wynikiem będzie 27

liczba = funkcja_oblicza(3.2)
print(liczba)
# wynikiem będzie 24.6
