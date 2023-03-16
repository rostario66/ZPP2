sekv = [1,2,3,4,5,6,7,8,9]

def mapovani(f,sekv):
    new_sez = []
    for i in sekv:
        new_sez.append(f(i))
    return new_sez

new_map = lambda x: x + x

print(mapovani(new_map,sekv))