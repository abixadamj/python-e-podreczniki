from turtle import *

def platek_1(bok):
    # n wynosi 1
    fd(bok)

def platek_2(bok):
    # n wynosi 2
    platek_1(bok/3)
    lt(60)
    platek_1(bok/3)
    rt(120)
    platek_1(bok/3)
    lt(60)
    platek_1(bok/3)

def platek_3(bok):
    # n wynosi 3
    platek_2(bok/3)
    lt(60)
    platek_2(bok/3)
    rt(120)
    platek_2(bok/3)
    lt(60)
    platek_2(bok/3)

platek_3(300)
