class Queue:
    def __init__(self):
        self.clear()

    def __del__(self):
        self.clear()

    def enQueue(self, data):
        self.state.append(data)

    def deQueue(self):
        if not self.isEmpty():
            value = self.state[0]
            del self.state[0]
            return value
        return -1

    def size(self):
        return len(self.state)

    def isEmpty(self):
        return not self.size()

    def clear(self):
        self.state = []