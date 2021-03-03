class Stack:
    def __init__(self):
        self.clear()

    def __del__(self):
        self.clear()

    def push(self, data):
        self.state.append(data)

    def pop(self):
        if not self.isEmpty():
            return self.state.pop()
        return -1

    def size(self):
        return len(self.state)

    def isEmpty(self):
        return not self.size()

    def clear(self):
        self.state = []