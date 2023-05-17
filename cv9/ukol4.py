def convert_number_to_bytes(number):
        bytes_array = []
        if number:
            while number:
                byte = number & 0xff
                bytes_array.append(byte)
                number = number >> 8
        else:
            bytes_array.append(0)
        return bytes_array[::-1]

bytes_array = convert_number_to_bytes(65536)
try:
    f = open("soubor.bin", "wb")
    f.write(bytes(bytes_array))
except:

    print("Chyba při práci se souborem.")
finally:
    f.close()


def convert_bytes_to_number(file):
    temp = []
    with open(file, "rb") as soubor:
        for i in soubor.read():
            temp.append(i)
    number = 0
    for byte in temp:
        number = number << 8
        number = number | byte
    return number


print(convert_bytes_to_number("soubor.bin"))


print(65530 >> 8)
print(65530 & 0xff)
print(bin(65700))
a = 65700
a1 = 65700 & 0xff
print()

print(bin(5300))
print(bin(5300 & 0xff))
print(bin(5300 >> 8))