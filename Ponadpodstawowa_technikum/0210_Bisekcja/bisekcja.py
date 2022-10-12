def wyznaczenie_bisekcji(a, b, epsilon):

    def f(x):
        # return (2*x**3) + (2*x) - 5
        return x**2 -2

    x = (a+b) / 2
    if f(x) == 0:
        return x
    else:
        while abs(a-b) > epsilon:
            x = (a+b) / 2
            # print('x, eps, f(x) ->',x,epsilon,abs(f(x)))
            if abs(f(x)) < epsilon:
                return x
            else:
                if f(a) * f(x) < 0:
                    b = x
                    # print('-',a,b)
                else:
                    a = x
                    # print('+',a,b)
        else:
            print('abs: a,b',a,b,'->',abs(a-b))
            return x

print(wyznaczenie_bisekcji(1,2,0.001))
print(wyznaczenie_bisekcji(1,2,0.000000000000001))
import math
print(math.sqrt(2))
print('**************')




def funkcja(x):
    return (2*x**3) + (2*x) - 5


def wyznaczenie_bisekcji_f(fun, a, b, epsilon):

    x = (a+b) / 2
    if fun(x) == 0:
        return x
    else:
        while abs(a-b) > epsilon:
            x = (a+b) / 2
            if abs(fun(x)) <= epsilon:
                return x
            elif fun(a) * fun(b) < 0:
                b = x
            else:
                a = x
        else:
            return x

def funkcja(x):
    return (2*x**3) + (2*x) - 5


def wyznaczenie_bisekcji_f(fun, a, b, epsilon):

    x = (a+b) / 2
    if fun(x) == 0:
        return x
    else:
        while abs(a-b) > epsilon:
            x = (a+b) / 2
            if abs(fun(x)) < epsilon:
                return x
            elif fun(a) * fun(x) < 0:
                b = x
            else:
                a = x

# print('-------------------------------')
# print(wyznaczenie_bisekcji_f(funkcja,-2000,2000,0.00000001))
# print(wyznaczenie_bisekcji_f(funkcja,-200,2000,0.00000001))

def testowa():

    def f_1(x):
        return 3*x**3 + 2*x**2 + 3 # x:[-2,-1)
    def f_2(x):
        return 2*x**2 -1 # x:[-1, 0)
    def f_3(x):
        return 2*x - 1.14 # x:[0, 1)

    def wyznaczenie_bisekcji_fn(fun, a, b, epsilon):
        b = b - epsilon # wyznaczamy przedział otwarty
        x = (a+b) / 2
        if fun(x) == 0:
            return x
        else:
            while abs(a-b) > epsilon:
                x = (a+b) / 2
                if abs(fun(x)) <= epsilon:
                    return x
                elif fun(a) * fun(b) < 0:
                    b = x
                else:
                    a = x
            else:
                return x

    f1 = wyznaczenie_bisekcji_fn(f_1, -2, -1, 0.00001)
    f2 = wyznaczenie_bisekcji_fn(f_2, -1, 0, 0.00001)
    f3 = wyznaczenie_bisekcji_fn(f_3, 0, 1, 0.00001)
    return [round(f1,5), round(f2,5), round(f3,5)]

print(testowa())
# [-1.5000126293182374, -0.7500101293182373, 0.4999873706817627]
[-1.50001, -0.75001, 0.49999]
