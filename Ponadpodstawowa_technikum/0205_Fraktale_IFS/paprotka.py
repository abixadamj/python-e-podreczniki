def paprotka_barnsleya(powtorzen=2000):
    from random import uniform
    import matplotlib.pyplot as plt
    X = []
    Y = []
    x, y = 0, 0
    for kolejny in range(powtorzen):
        q = uniform(0, 100)
        if q < 1:
            x = 0
            y = 0.16 * y
        elif q < 86:
            x = 0.85 * x + 0.04 * y
            y = -0.04 * x + 0.85 * y + 1.6
        elif q < 93:
            x = 0.2 * x - 0.26 * y
            y = 0.23 * x + 0.22 * y + 1.6
        else:
            x = -0.15 * x + 0.28 * y
            y = 0.26 * x + 0.24 * y + 0.44
        X.append(x)
        Y.append(y)
    # tworzenie wykresu - niebieskie znaki '+'
    print(len(X))
    plt.plot(X, Y, 'b+')
    plt.show()

paprotka_barnsleya(4000)
