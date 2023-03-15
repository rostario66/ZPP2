def interval(first,second):
    if first > second:
        return 0 
    else:
        return first + interval(first + 1, second)

print(interval(0,5))