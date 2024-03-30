import numpy as np


class GaußLegendre:
    def __init__(self, fis, cis, out):
        self.fis = fis
        self.cis = cis
        self.approx = out


def gaußLegendre(fx, a, b, n):

    cifi = np.polynomial.legendre.leggauss(n)
    sum = 0

    for i in range(len(cifi[0])):
        sum += fx((a + b) / 2 + (b - a) / 2 * cifi[0][i]) * cifi[1][i]

    out = (b - a) / 2 * sum

    rtn = GaußLegendre(cifi[0], cifi[1], out)

    return rtn
