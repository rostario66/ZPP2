def factorial_konc(n, a=1):
    if n == 0:
        return a
    else:
        return factorial_konc(n-1, a*n)

print(factorial_konc(4))
