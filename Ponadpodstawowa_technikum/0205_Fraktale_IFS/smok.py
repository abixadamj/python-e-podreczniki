def smok_heigewaya(powtorzen=3000):
    from random import randint
    import matplotlib.pyplot as plt
    X = []
    Y = []
    x, y = 0, 0
    for kolejny in range(powtorzen):
        q = randint(0, 1)
        if q == 1:
            x = -0.4 * x - 1
            y = -0.4 * y + 0.1
        else:
            x = 0.76 * x - 0.4 * y
            y = 0.4 * x + 0.76 * y
        X.append(x)
        Y.append(y)

    plt.plot(X, Y, 'b+')
    plt.show()



smok_heigewaya()