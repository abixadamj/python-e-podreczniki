from random import randint

# tworzymy zmienną zawierającą pustą listę
toto_lotek = []
print(f"Początkowo lista jest pusta: {toto_lotek}.")

# uruchamiamy pętlę iteracyjną
# wykona się 6 razy
for _ in range(6):
    # wewnątrz dodamy do listy kolejny element
    toto_lotek.append(randint(1,49))
    # wyśtietlimy za każdym razem jej zawartość
    print(f"Elementy listy to: {toto_lotek}.")

"""
Początkowo lista jest pusta: [].
Elementy listy to: [47].
Elementy listy to: [47, 38].
Elementy listy to: [47, 38, 1].
Elementy listy to: [47, 38, 1, 13].
Elementy listy to: [47, 38, 1, 13, 46].
Elementy listy to: [47, 38, 1, 13, 46, 25].    
"""
