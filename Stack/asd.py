import stack

stack = stack.Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.size())
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()

print(stack.state)

del stack