class Queue:
    def __init__(self):
        self.initialize()

    # queue 초기화
    def initialize(self):
        self.state = []

    # 데이터 삽입
    def enQueue(self, data):
        self.state.append(data)

    # 데이터 반환
    def deQueue(self):
        if self.isEmpty():
            return -1
        value = self.state[0]
        del self.state[0]
        return value

    # queue 길이
    def size(self):
        return len(self.state)

    # 비어있는지 확인
    def isEmpty(self):
        return not self.size()
        