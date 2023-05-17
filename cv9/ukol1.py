file = open(r"D:\vscodeProjects\zpp\matice.txt", "w", encoding='utf-8')

matrix = [[1,2,3,4,5],[4,5,6,7,8],[7,8,9,9,9,10]]

def save_matrix(matrix, soubor):
    for i in matrix:
        for j in range(len(i)):
            temp = str(i[j])
            soubor.write(temp)
            temp = int(temp)
            if j == len(i)-1:
                continue
            else:
                soubor.write(",")
        soubor.write("\n")
    soubor.close()

save_matrix(matrix, file)