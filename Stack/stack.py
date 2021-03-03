class Stack:
    def __init__(self):
        self.clear()

    def __del__(self):
        self.clear()

    def push(self, data):
        self.state.append(data)
        print(f"Push : {data}")

    def pop(self):
        if not self.isEmpty():
            value = self.state[-1]
            self.state.pop()
            print(f"Pop : {value}")
            return value
        print("Stack Is Empty")

    def size(self):
        return len(self.state)

    def isEmpty(self):
        return not self.size()

    def clear(self):
        self.state = []