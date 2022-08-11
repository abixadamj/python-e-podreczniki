def wartosc_znaku(znak):
    wartosc = ord(znak)
    if znak in ("eęyuioóaąEĘYUIOÓAĄ"):
        wartosc += 1
    return wartosc

informacja = input("Podaj informację: ")
suma_kontrolna = 0

for znak in informacja:
    suma_kontrolna += wartosc_znaku(znak)

print(f"Obliczona suma kontrolna wynosi {suma_kontrolna}")
