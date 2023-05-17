PREDCHOZI_PRVEK = 0
HODNOTA = 1
DALSI_PRVEK = 2
seznam = []

def pridej_do_obousmerneho_seznamu(seznam, x):
    predchozi_prvek = []
    while seznam:
        predchozi_prvek = seznam
        seznam = seznam[DALSI_PRVEK]
    seznam.extend([predchozi_prvek, x, []])

pridej_do_obousmerneho_seznamu(seznam,1)
pridej_do_obousmerneho_seznamu(seznam,2)
pridej_do_obousmerneho_seznamu(seznam,3)
pridej_do_obousmerneho_seznamu(seznam,4)
print(seznam)

def odeber_z_obousmerneho_seznamu(seznam, x):
    if seznam[HODNOTA] == x and seznam[DALSI_PRVEK]:
        seznam = seznam[DALSI_PRVEK]
        seznam[DALSI_PRVEK]
        seznam[PREDCHOZI_PRVEK] = []
    elif seznam[HODNOTA] == x and not seznam[DALSI_PRVEK]:
        seznam = []  
        return seznam
    current = seznam
    while current[DALSI_PRVEK]:
        if current[DALSI_PRVEK][HODNOTA] == x and current[DALSI_PRVEK][DALSI_PRVEK]:
            current[DALSI_PRVEK] = current[DALSI_PRVEK][DALSI_PRVEK]
            current[DALSI_PRVEK][PREDCHOZI_PRVEK] = current
            return seznam
        elif current[DALSI_PRVEK][HODNOTA] == x and not current[DALSI_PRVEK][DALSI_PRVEK]:
            current[DALSI_PRVEK] = []
            return seznam
        else:
            current = current[DALSI_PRVEK]
    return seznam

seznam = odeber_z_obousmerneho_seznamu(seznam, 1)
seznam = odeber_z_obousmerneho_seznamu(seznam, 3)
seznam = odeber_z_obousmerneho_seznamu(seznam, 2)

print(seznam)

pridej_do_obousmerneho_seznamu(seznam,4)
pridej_do_obousmerneho_seznamu(seznam,2)

print(seznam)