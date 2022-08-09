
def platek_kocha(z, stopien, dl_bok):

    def bok(stopien, dl_bok):
        if stopien == 0:
            z.forward(dl_bok)
        else:
            bok(stopien-1, dl_bok/3)
            z.left(60)
            bok(stopien-1, dl_bok/3)
            z.right(120)
            bok(stopien-1, dl_bok/3)
            z.left(60)
            bok(stopien-1, dl_bok/3)

    z.right(30)
    for i in range(3):
        bok(stopien, dl_bok)
        z.right(120)

    z.left(30)



from turtle import Turtle
zlw = Turtle()

zlw.penup()
zlw.goto(-100,200)
zlw.pendown()


platek_kocha(zlw,3,310)
while True:
    sleep(1)
    # CTRL+C - koniec
