def fibonacci_recursive(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_direct(n):
    sqrt_5 = 2.2360679775
    Phi = (1.0 + sqrt_5) / 2.0
    phi = (1.0 - sqrt_5) / 2.0


    return round((Phi**n - phi**n) / sqrt_5)


