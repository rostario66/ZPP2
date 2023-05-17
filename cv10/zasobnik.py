def vytvor_zasobnik():
    return []


def pridej_do_zasobniku(zasobnik, hodnota):
    return zasobnik.append(hodnota)


def odeber_ze_zasobniku(zasobnik):
    if not zasobnik:
        return None
    return zasobnik.pop()

