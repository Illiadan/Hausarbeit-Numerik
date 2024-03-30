class Trapez:
    def __init__(self, xis, yis, out):
        self.xis = xis
        self.yis = yis
        self.approx = out


def trapez(fx, a, b, n):
    yis = []
    xis = []
    sum = 0
    for i in range(n + 1):
        xi = a + i * (b - a) / n
        xis.append(xi)
    for xi in xis:
        yi = fx(xi)
        yis.append(yi)
    for i in range(len(yis)):
        if i == 0 or i == n:
            sum += yis[i]
        else:
            sum += 2 * yis[i]
    out = 0.5 * (b - a) / n * sum

    rtn = Trapez(xis, yis, out)

    return rtn
