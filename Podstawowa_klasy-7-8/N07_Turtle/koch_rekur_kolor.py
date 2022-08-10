from turtle import *
from random import choice
kolory = ["red", "green", "blue", "purple", "brown"]


def platek_stopien(bok, stopien):
    if stopien == 1:
        pencolor(choice(kolory))
        fd(bok)
    else:
        platek_stopien(bok/3, stopien-1)
        lt(60)
        platek_stopien(bok/3, stopien-1)
        rt(120)
        platek_stopien(bok/3, stopien-1)
        lt(60)
        platek_stopien(bok/3, stopien-1)


platek_stopien(1000, 5)
