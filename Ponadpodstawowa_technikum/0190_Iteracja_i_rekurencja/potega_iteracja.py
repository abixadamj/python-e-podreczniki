def potega_iter(podstawa, wykladnik):
    wynik = 1
    while wykladnik > 0:
        wynik = wynik * podstawa
        wykladnik -= 1
    return wynik


print(potega_iter(2,7))
