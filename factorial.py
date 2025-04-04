from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return 1 if n == 0 else n * factorial(n - 1)
