def NWD_odejmowanie_zliczanie_czas(x, y):
    from time import time
    t0 = time()
    ilosc = 0
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
        ilosc += 1


    print('Liczba',x,'; ilość odejmowań', ilosc, 'czas =',time()-t0)


def NWD_odejmowanie_zliczanie(x, y):
    ilosc = 0
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
        ilosc += 1

    print('Liczba',x,'; ilość odejmowań', ilosc)

def NWD_modulo_zliczanie(x, y):
    ilosc = 0
    while y > 0:
        modulo = x % y
        x = y
        y = modulo
        ilosc += 1

    print('Liczba',x,'; ilość dzieleń', ilosc)

# NWD_modulo_zliczanie(927566801,22)

def NWD_modulo_zliczanie_czas(x, y):
    from time import time
    t0 = time()
    ilosc = 0
    while y > 0:
        modulo = x % y
        x = y
        y = modulo
        ilosc += 1

    print('Liczba',x,'; ilość dzieleń', ilosc, 'czas =',time()-t0)

# wynik działania

# NWD_odejmowanie_zliczanie_czas(927566801,22)

# NWD_modulo_zliczanie_czas(927566801,22)
# Liczba 1 ; ilość dzieleń 3 czas = 1.430511474609375e-06
#
# # nawet dla bardzo dużej liczby działa błyskawicznie
# NWD_modulo_zliczanie_czas(922337203685477584,22)
# Liczba 2 ; ilość dzieleń 3 czas = 1.6689300537109375e-06
