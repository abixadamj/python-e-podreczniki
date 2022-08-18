# możemy definiować elementy list w kodzie programu
przedmioty_1 = [
    "język polski",
    "matematyka",
    "język angielski",
    "informatyka"
]

przedmioty_2 = [
    "wiedza o społeczeństwie",
    "biologia",
    "chemia",
    "wychowanie fizyczne"
]

przedmioty_3 = [
    "technika",
    "edukacja dla bezpieczeństwa",
    "etyka",
    "wychowanie do życia w rodzinie",
]

przedmioty_4 = [
    "muzyka",
    "historia",
    "geografia",
    "plastyka",
    "przyroda"
]

print(przedmioty_1)
print(przedmioty_2)
print(przedmioty_3)
print(przedmioty_4)

# możemy obliczyć ilość elementów w liście
ilosc_1 = len(przedmioty_1)
print(f"Przedmiotów w części 1 = {ilosc_1}")

ilosc_2 = len(przedmioty_2)
print(f"Przedmiotów w części 2 = {ilosc_2}")

ilosc_3 = len(przedmioty_3)
print(f"Przedmiotów w części 3 = {ilosc_3}")

ilosc_4 = len(przedmioty_4)
print(f"Przedmiotów w części 3 = {ilosc_4}")

# jeśli chcemy wywołać konretny element, używamy tzw. indeksu
przedmiot_a = przedmioty_1[3]
print(przedmiot_a)

przedmiot_b = przedmioty_2[2]
print(przedmiot_b)

przedmiot_c = przedmioty_3[1]
print(przedmiot_c)

przedmiot_d = przedmioty_4[3]
print(przedmiot_d)

# pierwszy element ma indeks 0 !!!
przedmiot_e = przedmioty_1[0]
print(przedmiot_e)

przedmiot_f = przedmioty_2[0]
print(przedmiot_f)

przedmiot_g = przedmioty_3[0]
print(przedmiot_g)

przedmiot_h = przedmioty_4[0]
print(przedmiot_h)

# ostatni element to ilość zwrócona funkcją len()-1 !!!
last_1 = len(przedmioty_1) - 1
przedmiot_i = przedmioty_1[last_1]
print(przedmiot_i)

last_2 = len(przedmioty_2) - 1
przedmiot_j = przedmioty_2[last_2]
print(przedmiot_j)

last_3 = len(przedmioty_3) - 1
przedmiot_k = przedmioty_3[last_3]
print(przedmiot_k)

last_4 = len(przedmioty_4) - 1
przedmiot_l = przedmioty_4[last_4]
print(przedmiot_l)

# Dzięki pętli iteracyjnej for możemy zwracać różne elementy listy:
print("Sprawdzamy parzyste elementy dla przedmioty_1:")
for indeks in range(0, len(przedmioty_1), 2):
    print(f"Indeks o wartości {indeks} -> element listy: {przedmioty_1[indeks]}")

print("Sprawdzamy nieparzyste elementy dla przedmioty_3:")
for indeks in range(1, len(przedmioty_3), 2):
    print(f"Indeks o wartości {indeks} -> element listy: {przedmioty_3[indeks]}")

# oraz dodawać je do nowej listy
nowa_lista_1 = []
for indeks in range(0, len(przedmioty_1), 2):
    nowa_lista_1.append(przedmioty_1[indeks])

nowa_lista_2 = []
for indeks in range(0, len(przedmioty_3), 2):
    nowa_lista_2.append(przedmioty_3[indeks])

print(nowa_lista_1)
print(nowa_lista_2)

# możemy tworzyć listę list , tzn. lista może być elementem innej listy
nowa_lista_3 = [nowa_lista_1, nowa_lista_2]
print(nowa_lista_3)

# ale aby stworzyć zupełnie nową listę, musimy użyć kopii list początkowych
nowa_lista_4 = [nowa_lista_1.copy(), nowa_lista_2.copy()]
print(nowa_lista_4)

# dodatkowo sprawdżmy, jak zachowuje się metoda sort()
print("Teraz wykonujemy sortowanie list")
przedmioty_1.sort()
przedmioty_2.sort()
przedmioty_3.sort()
przedmioty_4.sort()
print(przedmioty_1)
print(przedmioty_2)
print(przedmioty_3)
print(przedmioty_4)

# i zobaczmy, jak sortowanie wpływa na widoczność
nowa_lista_1.sort()
nowa_lista_2.sort()
print(nowa_lista_3)

# użycie indeksu poza zakresem generuje błąd
przedmiot_j = przedmioty_1[17]
print(przedmiot_j)
# przykładowy błąd wykonania
# Traceback (most recent call last):
#   File "multimedium.py", line 119, in <module>
#     przedmiot_j = przedmioty_1[17]

# wersja online do ćwiczeń (bez błędu)
# https://tinyurl.com/zpe-sp-python-listy
