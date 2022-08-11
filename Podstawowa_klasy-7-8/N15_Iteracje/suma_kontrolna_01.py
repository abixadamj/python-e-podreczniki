def wartosc_znaku(znak):
    return ord(znak)

informacja = input("Podaj informację: ")
suma_kontrolna = 0

for znak in informacja:
    suma_kontrolna += wartosc_znaku(znak)

print(f"Obliczona suma kontrolna wynosi {suma_kontrolna}")
