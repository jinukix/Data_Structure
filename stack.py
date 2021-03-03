class Stack:
    def __init__(self):
        self.state = []

    # 데이터 삽입
    def push(self, data):
        self.state.append(data)

    # 데이터 반환
    def pop(self):
        if self.isEmpty():
            return -1
        return self.state.pop()

    # stack 길이
    def size(self):
        return len(self.state)

    # 비어있는지 확인
    def isEmpty(self):
        return not self.size()

    # stack 비우기
    def clear(self):
        self.state = []