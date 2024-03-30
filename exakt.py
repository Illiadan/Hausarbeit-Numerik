from scipy import integrate


def exakt(fx, a, b):
    return integrate.quad(fx, a, b)
