sekvence = [-1,-2,-3,-4,-5,-6,-7,-8,-9]

def test_any(f,sekv):
    new_sekv = []
    for i in sekv:
        if f(i):
            return True
        else:
            return False
        
test = lambda x: x > 0

print(test_any(test,sekvence))



