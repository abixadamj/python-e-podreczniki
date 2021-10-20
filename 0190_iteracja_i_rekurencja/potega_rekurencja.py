def potega_rekur(podstawa, wykladnik):
    if wykladnik == 0:
        return 1
    else:
        if wykladnik % 2 == 1:
            return podstawa * potega_rekur(podstawa, wykladnik-1)
        else:
            return potega_rekur(podstawa, wykladnik/2) * potega_rekur(podstawa, wykladnik/2)


print(potega_rekur(2,7))
