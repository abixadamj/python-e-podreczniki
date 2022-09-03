stan_konta = 900
stan_bankomatu = 2500
odpowiednie_banknoty = True

podany_pin = input("Podaj PIN: ")

if podany_pin == "1234":
    print("PIN prawidłowy.")
    # PIN prawidłowy, wykonujemy dalsze instrukcje
    kwota = int(input("Podaj kwotę do wypłaty: "))
    if stan_konta >= kwota:
        # stan konta pozwala wypłacić pieniądze
        print("Masz odpowiednią sumę na koncie.")
        if stan_bankomatu >= kwota:
            # w bankomacie są pieniądze
            print("Bankomat ma odpowiednie środki.")
            if odpowiednie_banknoty == True:
                # są odpowiednie banknoty
                print("Wypłacamy banknoty z bankomatu.")
            else:
                print("Brak odpowiednich banknotów.")
        else:
            print("Bankomat nie ma takich pieniędzy.")
    else:
        print("Nie masz wystarczających środków.")
else:
    print("Podano BŁĘDNY PIN.")
