def bits_count(number):
    res = 0
    if number == 0:
        return 1
    if number < 0:
        number *= -1
        while number > 0:
            number = number >> 1
            res += 1
    while number > 0:
        number = number >> 1
        res += 1
    return res

print(bits_count(-15))

