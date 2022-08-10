def liczby_lotto():
    from random import randint
    liczby = ""

    for _ in range(6):
        liczby += str(randint(1,49)) + " "

    return liczby

# wykonujemy funkcję
print(liczby_lotto())
print(liczby_lotto())
print(liczby_lotto())

"""
# przykład wykonania
45 26 16 12 22 13
18 1 34 25 20 40
31 17 9 29 6 3
"""
