def test(a, b, c=3):
    print(a, b, c)


test(1, 2)


def factorial(n):
    if n == 1:
        return 1
    factorial_n_minus_1 = factorial(n=n - 1)
    return n * factorial_n_minus_1


print(factorial(5))
