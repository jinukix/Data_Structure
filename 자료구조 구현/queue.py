class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.initialize()

    # queue 초기화
    def initialize(self):
        self.head = None
        self.tail = None
        self.count = 0

    # 데이터 삽입
    def push(self, data):
        newNode = Node(data)

        if self.isEmpty():
            self.head = newNode
        else:
            self.tail.next = newNode

        self.tail = newNode
        self.count+=1

    # 데이터 추출
    def pop(self):
        if self.isEmpty():
            return -1

        if self.head == self.tail:
            value = self.head.data
            self.head = None
            self.tail = None
            self.count = 0

        tempNode = self.head
        value = tempNode.data
        self.head = tempNode.next
        self.count -= 1

        return value

    # 맨 앞 Node 데이터 반환
    def front(self):
        if self.isEmpty():
            return -1
        
        return self.head.data

    # 마지막 Node 데이터 반환
    def back(self):
        if self.isEmpty():
            return -1
        
        return self.tail.data

    # 비어있는지 확인
    def isEmpty(self):
        return not bool(self.count)

    # 전체 출력
    def printAll(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next
