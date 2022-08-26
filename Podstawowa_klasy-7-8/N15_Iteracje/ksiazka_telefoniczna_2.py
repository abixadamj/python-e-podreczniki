ksiazka_telefoniczna = ['Kamila Chwała',
    'Juliusz Małyszka', 'Gustaw Petrus',
    'Błażej Maszkiewicz', 'Jerzy Kowalówka',
    'Norbert Budzich', 'Julian Łaszcz',
    'Bruno Szmaj', 'Inga Madura', 'Kacper Dudała']

# zamierzony efekt:
# Osoba: 1 ==>> Kamila Chwała (kobieta)
# Osoba: 2 ==>> Juliusz Małyszka (mężczyzna)
# Osoba: 3 ==>> Gustaw Petrus (mężczyzna)
# Osoba: 4 ==>> Błażej Maszkiewicz (mężczyzna)
# Osoba: 5 ==>> Jerzy Kowalówka (mężczyzna)
# Osoba: 6 ==>> Norbert Budzich (mężczyzna)
# Osoba: 7 ==>> Julian Łaszcz (mężczyzna)
# Osoba: 8 ==>> Bruno Szmaj (mężczyzna)
# Osoba: 9 ==>> Inga Madura (kobieta)
# Osoba: 10 ==>> Kacper Dudała (mężczyzna)

osoba_nr = 1
for osoba in ksiazka_telefoniczna:
    tekst = f"Osoba: {osoba_nr} ==>> {osoba}"
    if osoba.split()[0].endswith("a"):
        tekst += " (kobieta)"
    else:
        tekst += " (mężczyzna)"
    print(tekst)
    osoba_nr += 1
