## badanie podzielności liczby


wprowadzona_liczba = int(input("Podaj dowolną liczbę naturalną:"))
reszta = wprowadzona_liczba % 2
if reszta == 0:
    print("Wprowadzona liczba jest parzysta.")
else:
    print("Wprowadzona liczba jest nieparzysta.")
    print("Reszta z dzielenia przez 2 wynosi:", reszta)


## Napisz program informujący czy liczba podana przez użytkownika jest
## większa, mniejsza czy równa zero. Pamiętaj o odpowiednich funkcjach
## wczytywania danych od użytkownika, o zmianie typu danych.
## Przemyśl, jakie instrukcje warunkowe i w jakiej kolejności możesz zastosować.

wprowadzona_liczba = int(input("Podaj dowolną liczbę całkowitą:"))
if wprowadzona_liczba > 0:
    print("Wprowadzona liczba jest dodatnia.")
if wprowadzona_liczba < 0:
    print("Wprowadzona liczba jest ujemna.")
if wprowadzona_liczba == 0:
    print("Wprowadzona liczba to zero.")


## silnik samochodu


print("Rozpoczynamy sekwencję uruchamiania silnika.")

if paliwo_jest_w_baku():
    print("OK, jest paliwo.... sprawdzimy teraz pasy bezpieczeństwa.")
    if zapiete_pasy_bezpieczenstwa():
        print("Super! Wiesz, jak jeździć bezpiecznie, zatem...")
        if kluczyk_w_stacyjce():
            print("Kluczyk w stacyjce, możesz ruszać... szerokiej drogi")
        else:
            print("Lecz nie zapomnij włożyć kluczyka do stacyjki...")
    else:
        print("Pasy są bardzo ważne - dopóki ich nie zapniesz, nie wolno ruszać samochodem!")
else:
    print("Bez paliwa nie ruszymy ;-(")


## komunikator internetowy, w serwisie ZPE.gov.pl funkcje działają, tu zapiszę
## ich definicje, aby kod był możliwy do uruchomienia w IDLE
## dostępne dane: login: "linux", hasło: "python"


def internet_dostepny():
    return True

def kontakt_z_serwerem():
    return True

def prawidlowy_login(login):
    return True if login == "linux" else False

def prawidlowe_haslo(login, haslo):
    return True if login == "linux" and haslo == "python" else False


print("Rozpoczynamy uruchomienie komunikatora.")

if internet_dostepny():
    print("Sieć internet działa prawidłowo... sprawdźmy serwer.")
    if kontakt_z_serwerem():
        print("Serwer dostępny.")
        login = input("Teraz podaj swój LOGIN UŻYTKOWNIKA: ")
        # w testerce ZPE musi być przypisanie wartości, bo input() nie działa
        # login = "linux"
        if prawidlowy_login(login):
            haslo = input("A teraz podaj HASŁO: ")
            # w testerce ZPE musi być przypisanie wartości, bo input() nie działa
            # haslo = "python"
            if prawidlowe_haslo(login, haslo):
                print("Witaj -", login,"- w naszej sieci społecznościowej.")
                print("Polecam się - https://Matrix.org")
            else:
                print("Niestety, hasło jest błędne.")
        else:
            print("Niestety, nie znam takiego użytkownika")
else:
    print("Brak Internetu - sprawdź połączenie.")
