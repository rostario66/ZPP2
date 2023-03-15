def delka(seznam):
    return delka1(seznam,0)

def delka1(seznam,a):
    if seznam == []:
        return a
    else:
        return delka1(seznam[1:],a+1)

print(delka(seznam = [1,2,3,4]))
