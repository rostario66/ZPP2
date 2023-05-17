file = open(r"D:\vscodeProjects\zpp\matice.txt", "rt", encoding='utf-8')


def po_znacich(soubor):
    a = 0
    while a != "":
        a = soubor.read(1)
        print(a, end="")


po_znacich(file)

