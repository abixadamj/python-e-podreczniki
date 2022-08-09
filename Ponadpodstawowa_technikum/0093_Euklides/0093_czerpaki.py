def czerpaki(a, b, c, ilosc_spr = 5):
    """a = 1sze naczynie
b = 2gie naczynie
c = pojemność naczynia docelowego
ilosc_spr = (domyślnie 5) liczba sprawdzeń w pętli
"""

    def NWD(x, y):
        while y > 0:
            modulo = x%y
            x = y
            y = modulo
        return x

    def spr_eval(fun, k, c, znak, ilosc_spr):
        for A in range(1, ilosc_spr+1, k):
            for B in range(1, ilosc_spr+1, k):
                if eval(fun) == c:
                    return 1, f"OK dla ilości: {A} naczyń poj. {a} {znak} {B} naczyń poj. {b} = {c}"
        else:
             return 0, "Brak rozwiązania"


    # obliczamy NWD, które będzie krokiem dla pętli sprawdzającej
    k = NWD(a, b)

    # zamiana miejscami jeśli pierwsza wartość mniejsza od drugiej
    if a < b:
        a, b = b, a

    znak = "-"
    fun = "A*a - B*b"
    wynik = spr_eval(fun, k, c, znak, ilosc_spr)
    if wynik[0]:
        return wynik[1]

    znak = "+"
    fun = "A*a + B*b"
    wynik = spr_eval(fun, k, c, znak, ilosc_spr)
    if wynik[0]:
        return wynik[1]

    return "Brak rozwiązań"

# przykład
print(czerpaki(16,22,4))
print(czerpaki(16,22,4,10))
# Brak rozwiązań

print(czerpaki(16,20,4))
print(czerpaki(3,3,18,10))
# OK dla ilości: 1 naczyń poj. 20 - 1 naczyń poj. 16 = 4
# OK dla ilości: 7 naczyń poj. 3 - 1 naczyń poj. 3 = 18
