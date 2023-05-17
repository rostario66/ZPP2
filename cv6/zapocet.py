def vytvor_matici(pocet_radku, pocet_sloupcu):
    return [pocet_radku, pocet_sloupcu, None, None]

def vloz_prvek(matice, prvek, radek, sloupec):
    if prvek == 0:
        return
    pocet_radku = matice[0]
    pocet_sloupcu = matice[1]

    if radek < 0 or radek >= pocet_radku:
        return print("zadany index radku ve matice neexistuje")
    elif sloupec < 0 or sloupec >= pocet_sloupcu:
        return print("zadany index sloupce ve matice neexistuje")

    def najdi_nebo_vytvor(list_name, index):
        predchozi, aktualni = None, list_name
        while aktualni and aktualni[0] != index:
            predchozi, aktualni = aktualni, aktualni[1]

        if not aktualni:
            aktualni = [index, None, None]
            if predchozi:
                predchozi[1] = aktualni
            else:
                list_name = aktualni
        return list_name, aktualni

    matice[2], radek_element = najdi_nebo_vytvor(matice[2], radek)
    matice[3], sloupec_element = najdi_nebo_vytvor(matice[3], sloupec)

    radek_element[2] = [sloupec, prvek, radek_element[2]]
    sloupec_element[2] = [radek, prvek, sloupec_element[2]]

def najdi_hodnotu(radky, radek, sloupec):
    aktualni_radek = radky
    while aktualni_radek and aktualni_radek[0] != radek:
        aktualni_radek = aktualni_radek[1]

    if not aktualni_radek:
        return 0

    hodnoty = aktualni_radek[2]
    while hodnoty and hodnoty[0] != sloupec:
        hodnoty = hodnoty[2]

    if not hodnoty:
        return 0

    return hodnoty[1]


def zobraz_matici(matice):
    pocet_radku, pocet_sloupcu, radky, sloupce = matice
    for i in range(pocet_radku):
        radek = []
        for j in range(pocet_sloupcu):
            hodnota = najdi_hodnotu(radky, i, j)
            radek.append(hodnota)
        print(" ".join("{:3}".format(k) for k in radek))


matice = vytvor_matici(4, 4)

vloz_prvek(matice, 13, 0, 4)
vloz_prvek(matice, 18, 0, 3)
vloz_prvek(matice, 1, 1, 2)
vloz_prvek(matice, 4, -1, 0)
vloz_prvek(matice, 11, 3, 2)
vloz_prvek(matice, 5, 0, 2)
vloz_prvek(matice, 7, 0, 2)

zobraz_matici(matice)
