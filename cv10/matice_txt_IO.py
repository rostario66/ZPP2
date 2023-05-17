M = [[1,2,3,5,5], [4,5,6,4,4], [7,8,5,3,3]]

def uloz_matici(matice, M):
    matice = open(matice, "w", encoding="utf-8")
    for i in M:
        for j in range(len(i)):
            temp = str(i[j])
            matice.write(temp)
            temp = int(temp)
            if j == len(i)-1:
                continue
            else:
                matice.write(",")
        matice.write("\n")
    matice.close()

def nacti_matici(matice):
    soubor = open(matice, "rt", encoding="utf-8")
    radek = soubor.readlines()
    list_1 = []
    for i in radek:
        new = i.split(",")
        list_2 = []
        for i in new:
            list_2.append(int(i))
        list_1.append(list_2)
    return list_1

