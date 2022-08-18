# wczytujemy funkcję
from pickle import dump

# definiujemy pustą listę przedmiotów i ocen w tych przedmiotach
lista_przedmiotow = []
oceny_przedmiotow = []

def dodaj_oceny(nazwa_przedmiotu):
    # definiujemy prostą listę
    oceny = []
    print(f"Dodajemy oceny dla {przedmiot} - wartość 0 kończy dodawanie.")
    # używamy pętli warunkowej działającej w nieskończoność
    while True:
        ocena = int(input("Podaj ocenę: "))
        if ocena == 0:
            # przerywamy działanie pętli
            break
        # jesli nie przerwaliśmy, to dodajemy ocenę do listy ocen
        # jeśli ocena jest jedną z kilku możliwych
        # używamy tu operatora in, który sprawdza obecność argumentu w sekwencji
        if ocena in [1, 2, 3, 4, 5, 6]:
            oceny.append(ocena)
    # koniec pętli po break
    print(f"Wczytaliśmy {len(oceny)} ocen: {oceny}")
    return oceny


# uruchamiamy pętlę iteracyjną
# wykona się 6 razy
for _ in range(6):
    # element wvczytamy z klawiatury
    przedmiot = input("Podaj nazwę przedmiotu: ")
    # wewnątrz dodamy do listy kolejny element
    # używamy wbudowanego w Pythnie sposobu - metody LISTA.append()
    lista_przedmiotow.append(przedmiot)
    # wyświetlimy za każdym razem jej zawartość
    print(f"Elementy listy to: {lista_przedmiotow}.")

# teraz dla każdego przedmiotu wczytamy oceny do oceny_przedmiotow
for przedmiot in lista_przedmiotow:
    # wywołujemy funkcję, która zwraca listę ocen
    tymczasowe_oceny = dodaj_oceny(przedmiot)
    # i dodajemy ją jako kopię do pełnej listy
    oceny_przedmiotow.append(tymczasowe_oceny.copy())

# na końcu wyświetlamy wszystkie elementy
# możemy wykorzystać fakt, że obie listy: nazw przedmiotów i ocen
# zachowują kolejność wprowadzania danych
# wykorzystamy odwołanie się do elementu listy po tzw. indeksie, który
# w Pythonie liczony jest od zera.

# wiemy, że w naszym przypadku mamy 6 przedmiotów, ale sprawdzimy to
ilosc_przedmiotow = len(lista_przedmiotow)

for kolejny_indeks in range(ilosc_przedmiotow):
    nazwa_przedmiotu = lista_przedmiotow[kolejny_indeks]
    oceny_przedmiotu = oceny_przedmiotow[kolejny_indeks]
    print(f"Dla przedmiotu {nazwa_przedmiotu} zapamiętane oceny to: {oceny_przedmiotu}")

# tworzymy główną listę, która zawiera dwa elementy
# obie listy
dziennik_elektroniczny = [lista_przedmiotow, oceny_przedmiotow]

# zapisujemy do pliku do późniejszego wykorzystania
with open("dziennik_elektroniczny.dat", "wb") as plik:
    dump(dziennik_elektroniczny, plik)
    print("Zapisałem dane do pliku.")
