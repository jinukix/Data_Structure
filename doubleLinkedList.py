class Node:
    def __init__(self, data):
        self.data = data
        self.front = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.initialize()

    # 초기화
    def initialize(self):
        self.__head = None
        self.__tail = None

    # Node 맨 마지막에 추가
    def push_Back(self, data):
        newNode = Node(data)

        if self.isEmpty():
            self.__head = newNode
            self.__tail = newNode
            return

        newNode.front = self.__tail
        self.__tail.next = newNode
        self.__tail = newNode

    # Node 맨 앞에 추가
    def push_Front(self, data):
        newNode = Node(data)

        if not self.getListSize():
            self.__head = newNode
            self.__tail = newNode
            return
    
        newNode.next = self.__head
        self.__head.front = newNode
        self.__head = newNode

    # 맨 마지막 Node 반환
    def pop_Back(self):
        value = self.__tail.data
        self.__tail = self.__tail.front
        self.__tail.next = None

        return value

    # 맨 앞 Node 반환
    def pop_Front(self):
        value = self.__head.data
        self.__head = self.__head.next
        self.__head.front = None

        return value

    # 비어있는지 확인.
    def isEmpty(self):
        return not self.__head

    # index번째에 Node삽입
    def insert(self, index, data):
        size = self.getListSize()
        if index > size or index < 0:
            return -1

        if index == size:
            self.push_Back(data)
            return

        if not index: # 0번째 index
            self.push_Front(data)
            return

        tempNode = self.__head
        prevNode = tempNode.front

        for _ in range(index):
            tempNode = tempNode.next
            prevNode = tempNode.front

        newNode = Node(data)

        newNode.front = prevNode
        prevNode.next = newNode

        newNode.next = tempNode
        tempNode.front = newNode

    # index번째 Node 삭제
    def deleteNode(self, index):
        size = self.getListSize()
        # insert의 경우 index가 getListSize()만큼 들어와도 삽입이 되지만 delete의 경우에는 불가능
        if index + 1 > size or index < 0: 
            return -1

        if index == size - 1:
            self.pop_Back()
            return

        if not index: # 0번째 index
            self.pop_Front()
            return

        tempNode = self.__head
        prevNode = tempNode.front

        for _ in range(index):
            tempNode = tempNode.next
            prevNode = tempNode.front

        prevNode.next = tempNode.next
        tempNode.next.front = prevNode
        
    # 사이즈 반환
    def getListSize(self):
        size = 0
        tempNode = self.__head

        while tempNode:
            size += 1
            tempNode = tempNode.next

        return size

    # 전체 출력
    def printAll(self):
        tempNode = self.__head

        while tempNode:
            print(tempNode.data)
            tempNode = tempNode.next