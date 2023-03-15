def power(base,expo,a = 1):
    if expo == 0:
        return a
    else:
        return power(base,expo -1, a*base)

print(power(2,8))
