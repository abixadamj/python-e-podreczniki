zmienna = 9
while zmienna:
    print("Zmienna=", zmienna)
    zmienna -= 1

# efekt
# Zmienna= 9
# Zmienna= 8
# Zmienna= 7
# Zmienna= 6
# Zmienna= 5
# Zmienna= 4
# Zmienna= 3
# Zmienna= 2
# Zmienna= 1

# przykład 2 - przerwanie za pomocą break
zmienna = 99
while zmienna:
    print("Zmienna=", zmienna)
    zmienna -= 1
    if zmienna < 90:
        break

# efekt
# Zmienna= 99
# Zmienna= 98
# Zmienna= 97
# Zmienna= 96
# Zmienna= 95
# Zmienna= 94
# Zmienna= 93
# Zmienna= 92
# Zmienna= 91
# Zmienna= 90

# przykład 3 - pętla nieskończona - wyamaga użycia break
zmienna = 5
while True:
    print("Zmienna=", zmienna)
    zmienna -= 1
    if zmienna < -3:
        break

# efekt
# Zmienna= 5
# Zmienna= 4
# Zmienna= 3
# Zmienna= 2
# Zmienna= 1
# Zmienna= 0
# Zmienna= -1
# Zmienna= -2
# Zmienna= -3
