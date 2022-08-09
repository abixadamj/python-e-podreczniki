podany_pin = input("Proszę podać PIN: ")

if podany_pin == "1234":
    print("PIN prawidłowy.")
    # tu wykonujemy dalsze instrukcje
    kwota = int(input("Podaj kwotę do wypłaty: "))
    if ile_jest_pieniedzy_na_koncie() > kwota:
        # wypłacamy
        if ile_jest_pieniedzy_w_bankomacie() > kwota:
            # sprawdzamy czy są odpowiednie banknoty
            if sa_odpowiednie_banknoty(kwota) == True:
                # teraz spełnione są warunki
                print("Wypłacamy banknoty z bankomatu.")
else:
    print("Podano BŁĘDNY PIN")
    # tu przerywamy działanie
