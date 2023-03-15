def pascal(row, column):
    if column == 0 or column == row:
        return 1
    else:
        return pascal(row - 1, column - 1) + pascal(row - 1, column)
print(pascal(7,2))