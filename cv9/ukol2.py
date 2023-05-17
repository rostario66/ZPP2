file = open(r"D:\vscodeProjects\zpp\text1.txt", "r", encoding='utf-8')

def load_matrix(soubor):
    soubor = file.readlines()
    list_1 = []
    for i in soubor:
        new = i.split(",")
        list_2 = []
        for i in new:
            list_2.append(int(i))
        list_1.append(list_2)
    return list_1


a = (load_matrix(file))
print(a[0][0])

