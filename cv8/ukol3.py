def rotate_right(number, count):
    number = bin(number)
    number = number[2:]
    first = number[count:]
    second = number[:count]
    return first + second
    

number = 0b101011
count = 2

print(rotate_right(number, count))