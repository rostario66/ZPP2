import zasobnik

z1 = zasobnik.vytvor_zasobnik()

zasobnik.pridej_do_zasobniku(z1, "world")
zasobnik.pridej_do_zasobniku(z1, "Hello")
z2 = zasobnik.vytvor_zasobnik()
zasobnik.pridej_do_zasobniku(z2, "fist")
zasobnik.pridej_do_zasobniku(z2, "second")
z3 = zasobnik.vytvor_zasobnik()

print(zasobnik.odeber_ze_zasobniku(z1))
print(zasobnik.odeber_ze_zasobniku(z1))
print(zasobnik.odeber_ze_zasobniku(z2))
print(zasobnik.odeber_ze_zasobniku(z2))

print(zasobnik.odeber_ze_zasobniku(z1))
print(zasobnik.odeber_ze_zasobniku(z2))
print(zasobnik.pridej_do_zasobniku(z3, "3131"))
print(zasobnik.odeber_ze_zasobniku(z3))
zasobnik.pridej_do_zasobniku(z1,16)
print(zasobnik.odeber_ze_zasobniku(z1))