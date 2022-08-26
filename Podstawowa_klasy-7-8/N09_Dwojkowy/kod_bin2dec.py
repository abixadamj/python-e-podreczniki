def liczba_lista(liczba):
    lista = []
    while liczba > 0:
        cyfra = liczba % 10
        lista.append(cyfra)
        liczba = liczba // 10
    return lista


def dziesietny(lista):
    lista_dziesietna = []
    wykladnik = 0
    for cyfra in lista:
        lista_dziesietna.append(2 ** wykladnik * cyfra)
        wykladnik += 1
    return lista_dziesietna


def dwojkowy_dziesietny(liczba):
    liczba_dzisietna = 0
    wykladnik = 0
    while liczba > 0:
        cyfra = liczba % 10
        liczba_dzisietna += 2 ** wykladnik * cyfra
        wykladnik += 1
        liczba = liczba // 10
    return liczba_dzisietna


liczba = 1011010
lista_cyfr = liczba_lista(liczba)
lista_dziesietna = dziesietny(lista_cyfr)
dwojk_dzies_lista = int(str(liczba), base=2)
dwojkowy_na_dziesietny = dwojkowy_dziesietny(liczba)

print(
    liczba,
    lista_cyfr,
    lista_dziesietna,
    sum(lista_dziesietna),
    dwojkowy_na_dziesietny,
    dwojk_dzies_lista,
    sep=" --> "
)
