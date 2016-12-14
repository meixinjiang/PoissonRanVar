"""
Generates a Poisson random variable using the inversion sampling method.
Algorithm taken from wikipedia.
parameters - rate
returns - Poisson random variable
"""
def poissonRanVar(rate):
    x = 0
    p = exp(-rate)
    s = p
    u = random()
    while u > s:
        x += 1
        p = p * rate / x
        s += p
    return x
