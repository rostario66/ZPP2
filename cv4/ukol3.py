stack = []

def push(i):
    stack.append(i)

def pop():
    if len(stack) == 0:
        return None
    return stack.pop()

def print_stack():
    print("Stack:", end=" ")
    for i in stack:
        print(i, end=" ")
    print()

queue = []

def enqueue(element):
    queue.append(element)

def dequeue():
    if len(queue) == 0:
        return None
    return queue.pop(0)

def print_queue():
    print("Queue:", end=" ")
    for i in queue:
        print(i, end=" ")
    print()


push(1)
push(2)
push(3)
print_stack()
pop()
pop()
print_stack()
pop()
pop()
push(2)

enqueue(3)
enqueue(4)
enqueue(17)
print_queue()
dequeue()
print_queue()