import zasobnik

z1 = zasobnik.vytvor_zasobnik(2)

zasobnik.pridej_do_zasobniku(z1, 444)
zasobnik.pridej_do_zasobniku(z1, 1010)
zasobnik.pridej_do_zasobniku(z1, 5000)
zasobnik.zapis_do_souboru("zasobnik.bin", z1)


z2 = zasobnik.nacti_ze_souboru("zasobnik.bin")

z3 = zasobnik.vytvor_zasobnik(3)
zasobnik.pridej_do_zasobniku(z3, 900)
zasobnik.pridej_do_zasobniku(z3, 8000)
zasobnik.pridej_do_zasobniku(z3, 9898)

zasobnik.zapis_do_souboru("zasobnik.bin", z3)
z4 = zasobnik.nacti_ze_souboru("zasobnik.bin")


z5 = zasobnik.nacti_ze_souboru("zasobnik.bin")
print(z5)
zasobnik.zapis_do_souboru("zasobnik.bin", z2)

z5 = zasobnik.nacti_ze_souboru("zasobnik.bin")
print(z5)
zasobnik.pridej_do_zasobniku(z5, 65534)
print(z5)

