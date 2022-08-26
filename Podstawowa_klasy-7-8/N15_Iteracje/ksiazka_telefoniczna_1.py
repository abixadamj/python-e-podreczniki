ksiazka_telefoniczna = ['Kamila Chwała',
    'Juliusz Małyszka', 'Gustaw Petrus',
    'Błażej Maszkiewicz', 'Jerzy Kowalówka',
    'Norbert Budzich', 'Julian Łaszcz',
    'Bruno Szmaj', 'Inga Madura', 'Kacper Dudała']

# zamierzony efekt:
# Osoba: 1 ==>> Kamila Chwała
# Osoba: 2 ==>> Juliusz Małyszka
# Osoba: 3 ==>> Gustaw Petrus
# Osoba: 4 ==>> Błażej Maszkiewicz
# Osoba: 5 ==>> Jerzy Kowalówka
# Osoba: 6 ==>> Norbert Budzich
# Osoba: 7 ==>> Julian Łaszcz
# Osoba: 8 ==>> Bruno Szmaj
# Osoba: 9 ==>> Inga Madura
# Osoba: 10 ==>> Kacper Dudała


osoba_nr = 1
for osoba in ksiazka_telefoniczna:
    print(f"Osoba: {osoba_nr} ==>> {osoba}")
    osoba_nr += 1
