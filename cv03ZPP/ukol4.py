sekvence = [1,2,3]

def aplikuj(f,sekv):
    dop = 0
    result = 0
    for i in sekv:
        result += f(dop,i)
    return result   

        
anon_aplikuj = lambda x,y: x + y

print(aplikuj(anon_aplikuj, sekvence))