# tworzymy zmienną zawierającą pustą listę
lista_przedmiotow = []
print(f"Początkowo lista jest pusta: {lista_przedmiotow}.")

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
