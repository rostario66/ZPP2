HODNOTA = 0
DALSI_PRVEK = 1
seznam = []

def pridej_do_seznamu(seznam, x):
        while seznam:
            seznam = seznam[DALSI_PRVEK]
        seznam.extend([x, []])

pridej_do_seznamu(seznam,1)
pridej_do_seznamu(seznam,2)
pridej_do_seznamu(seznam,3)

def odeber_ze_seznamu(seznam, x):
        for i range(len(seznam)):
            if seznam[HODNOTA] == x:
               seznam.pop(x)
            else:
                seznam = seznam[DALSI_PRVEK]
        return seznam

print(odeber_ze_seznamu(seznam, 2))




            



