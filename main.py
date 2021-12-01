from math import *

expression = "cos(x) + x ** 3 - log10(x) - pi"


def f(x: float) -> float:
    try:
        return eval(expression)
    except ValueError:
        return f(x + 1E-3)


def deriv(x: float) -> float:
    # using first principles (avoiding ZeroDivision)
    h = 1E-10
    return float("%.4f" % ((f(x + h) - f(x)) / h))


def newton(f: __import__("typing").Callable) -> float:
    xi = 0
    for _ in range(1, 1001):
        try:
            xi -= f(xi) / deriv(xi)
        except ZeroDivisionError:
            xi += 0.25
    if not -1E-10 < f(xi) < 1E-10:
        a = False
        try:
            a = f(0) != 0
        finally:
            if a:
                raise Exception("No real roots")
    return xi if f(0) != 0 else 0.0


print(newton(f))
