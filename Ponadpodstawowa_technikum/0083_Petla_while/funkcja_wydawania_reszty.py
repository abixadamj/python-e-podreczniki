def _funkcja(kwota):
    zwracana_wartosc = {}
    if kwota <= 0:
        return False
    else:
        pozostalo = kwota
        while pozostalo > 49:
            if pozostalo > 399:
                _400 = pozostalo // 400
                zwracana_wartosc[400] = _400
                pozostalo -= _400 * 400
            elif pozostalo > 199:
                _200 = pozostalo // 200
                zwracana_wartosc[200] = _200
                pozostalo -= _200 * 200
            elif pozostalo > 49:
                _50 =  pozostalo // 50
                zwracana_wartosc[50] = _50
                pozostalo -= _50 * 50
        else:
            zwracana_wartosc[1] = pozostalo
        return zwracana_wartosc
