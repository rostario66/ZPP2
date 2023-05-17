def convert(letter):
    temp = ord(letter)
    temp = temp ^ 32
    return chr(temp)
        


print(convert("D")) 

