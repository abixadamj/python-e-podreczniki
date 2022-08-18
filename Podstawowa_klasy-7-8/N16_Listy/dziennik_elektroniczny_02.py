# wczytujemy funkcję
from pickle import load

with open("dziennik_elektroniczny.dat", "rb") as plik:
    dziennik_elektroniczny = load(plik)
    print("Wczytałem dane z pliku.")


# przypisujemy poszczególnym listom wartości wczytane z pliku
lista_przedmiotow, oceny_przedmiotow = dziennik_elektroniczny

# na końcu wyświetlamy wszystkie elementy
# możemy wykorzystać fakt, że obie listy: nazw przedmiotów i ocen
# zachowują kolejność wprowadzania danych
# wykorzystamy odwołanie się do elementu listy po tzw. indeksie, który
# w Pythonie liczony jest od zera.

# sprawdzami ilość przedmiotów
ilosc_przedmiotow = len(lista_przedmiotow)

for kolejny_indeks in range(ilosc_przedmiotow):
    nazwa_przedmiotu = lista_przedmiotow[kolejny_indeks]
    oceny_przedmiotu = oceny_przedmiotow[kolejny_indeks]
    print(f"Dla przedmiotu {nazwa_przedmiotu} zapamiętane oceny to: {oceny_przedmiotu}")
