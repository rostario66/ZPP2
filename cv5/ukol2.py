root = []

PARENT = 0
VALUE = 1
LEFT_CHILD = 2
RIGHT_CHILD = 3

def tree_add(node, x):
    if not node:
        node.extend([[], x, [], []])
        return
        
    while node[VALUE] != x:
        if x < node[VALUE]:
            if node[LEFT_CHILD]:
                node = node[LEFT_CHILD]
            else:
                node[LEFT_CHILD] = [node, x, [], []]
                return
                    
        elif x > node[VALUE]:
            if node[RIGHT_CHILD]:
                node = node[RIGHT_CHILD]
            else:
                node[RIGHT_CHILD] = [node, x, [], []]
                return
                
tree_add(root, 8)
tree_add(root, 4)
tree_add(root, 23)
tree_add(root, 16)
tree_add(root, 15)
tree_add(root, 42)
tree_add(root, 17)
print(root)