class Simpson:
    def __init__(self, xis, yis, out):
        self.xis = xis
        self.yis = yis
        self.approx = out


def simpson(fx, a, b, n):
    yis = []
    xis = []
    sum = 0
    for i in range(2 * n + 1):
        xi = a + i * (b - a) / (2 * n)
        xis.append(xi)
    for xi in xis:
        yi = fx(xi)
        yis.append(yi)
    for i in range(len(yis)):
        if i == 0 or i == 2 * n:
            sum += yis[i]
        elif i % 2 == 1:
            sum += 4 * yis[i]
        else:
            sum += 2 * yis[i]
    out = (b - a) / (6 * n) * sum

    rtn = Simpson(xis, yis, out)

    return rtn
