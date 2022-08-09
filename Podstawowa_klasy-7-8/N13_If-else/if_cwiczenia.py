wprowadzona_liczba = int(input("Podaj dowolną liczbę naturalną:"))
reszta = wprowadzona_liczba % 2
if reszta == 0:
    print("Wprowadzona liczba jest parzysta.")
else:
    print("Wprowadzona liczba jest nieparzysta.")
    print(f"Reszta z dzielenia przez 2 wynosi: {reszta}")

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


# komunikator internetowy

print("Rozpoczynamy uruchomienie komunikatora.")

if internet_dostepny():
    print("Sieć internet działa prawidłowo... sprawdźmy serwer.")
    if kontakt_z_serwerem():
        print("Serwer dostępny.")
        login = input("Teraz podaj swój LOGIN UŻYTKOWNIKA: ")
        if prawidlowy_login(login):
            haslo = input("A teraz podaj HASŁO: ")
            if prawidlowe_haslo(login, haslo):
                print(f"Witaj - {login} - w naszej sieci społecznościowej.")
                print("Polecam się - https://Matrix.org")
        else:
            print("Niestety, nie znam takiego użytkownika")
else:
    print("Brak Internetu - sprawdź połączenie.")
