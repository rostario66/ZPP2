sekvence = [1,-2,3,-4,-5,-6,-7,8,-9]

def test_all(f, sekv):
    for element in sekv:
        if not f(element):
            return False
    return True

      
test = lambda x: x > 0

print(test_all(test,sekvence))
