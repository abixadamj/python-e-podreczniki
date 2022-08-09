kwota = int(input('Podaj kwotę do wypłaty: '))
do_wydania = {}
do_wydania['500'] = 0
do_wydania['200'] = 0
do_wydania['50'] = 0
if kwota % 50 > 0:
    kwota = 0
while kwota > 0:

    if kwota > 500:
        banknoty_500 = kwota // 500
        do_wydania['500'] = banknoty_500
        kwota -= kwota % 500

    if kwota > 200:
        banknoty_200 = kwota // 200
        do_wydania['200'] = banknoty_200
        kwota -= kwota % 200

    if kwota > 50:
        banknoty_50 = kwota // 50
        do_wydania['50'] = banknoty_50
        kwota -= kwota % 50

print('banknoty: ', do_wydania)
