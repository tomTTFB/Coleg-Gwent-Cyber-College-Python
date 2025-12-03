# Stacks

stack = []

stack.append('A')
stack.append('B')
stack.append('C')
print("Stack after pushes:", stack)

popped = stack.pop()
print("Popped element:", popped)
print("Stack after pop:", stack)

stack.append('C')
stack.append('D')
print("Stack after more pushes:", stack)