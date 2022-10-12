def palindrom_petla(tekst):
    dl = len(tekst)
    j = dl
    for i in range(dl):
        if tekst[i] != tekst[dl -i]:
            return False
    else:
        return True

def testowa(wyrazenie):
    dl = len(wyrazenie)
    for znak in '!@#$%^&*(){}[]-_=+|`~,<.>/?;: ':
        wyrazenie = wyrazenie.replace(znak,'')
    wyrazenie = wyrazenie.lower()
    palindrom = wyrazenie == wyrazenie[::-1]
    return [palindrom, dl, len(wyrazenie)]



wynik = testowa('ala^%ama(ala@!;:><.,ddd')
print(wynik)
print(type(wynik) is list)
wynik = testowa('ala^%ama(ala@!;:><.,')
print(wynik)
print(type(wynik) is list)


[False, 23, 12]
True
[True, 20, 9]
True
