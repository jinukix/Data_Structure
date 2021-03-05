class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularList:
    def __init__(self):
        self.initialize()

    # 초기화    
    def initialize(self):
        self.__tail = None

    # Node 추가 
    def addNode(self, data):
        newNode = Node(data)

        if self.isEmpty():
            self.__tail = newNode
            newNode.next = self.__tail
            return

        newNode.next = self.__tail.next
        self.__tail.next = newNode
        self.__tail = newNode
        
    # index번째에 Node 삽입
    def insertNode(self, index, data):
        size = self.getListSize()
        if index > size or index < 0:
            return -1

        if index == size:
            self.addNode(data)
            return

        NewNode = Node(data)

        tempNode = self.__tail.next
        prevNode = self.__tail

        for _ in range(index):
            prevNode = tempNode
            tempNode = tempNode.next

        NewNode.next = tempNode
        prevNode.next = NewNode

    # data값을 가진 Node 1개 삭제
    def deleteNodeData(self, data):
        if self.isEmpty():
            return -1

        tempNode = self.__tail.next
        prevNode = self.__tail

        while tempNode != self.__tail:
            if tempNode.data == data:
                prevNode.next = tempNode.next
                return

            prevNode = tempNode
            tempNode = tempNode.next
        
        if tempNode.data == data:
            prevNode.next = tempNode.next
            self.__tail = prevNode
            
        return -1
            
    # index번째 Node 삭제
    def deleteNodeIndex(self, index):
        size = self.getListSize()
        if index > size or index < 0:
            return -1

        tempNode = self.__tail.next
        prevNode = self.__tail
        
        for _ in range(index):
            prevNode = tempNode
            tempNode = tempNode.next

        if tempNode == self.__tail:
            prevNode.next = tempNode.next
            self.__tail = prevNode
            return

        prevNode.next = tempNode.next
        
    # index 번째 Node data 반환
    def getNodeData(self, index):
        if index > self.getListSize() or index < 0:
            return -1

        tempNode = self.__tail.next

        for _ in range(index):
            tempNode = tempNode.next

        return tempNode.data

    # 사이즈 반환
    def getListSize(self):
        if self.isEmpty():
            return 0

        size = 1
        tempNode = self.__tail.next

        while tempNode != self.__tail:
            size += 1
            tempNode = tempNode.next
        return size
        
    # 비어있는지 확인.
    def isEmpty(self):
        return not self.__tail
    
    # 전체 출력
    def printAll(self):
        if self.isEmpty():
            return 

        tempNode = self.__tail.next

        while tempNode != self.__tail:
            print(tempNode.data)
            tempNode = tempNode.next
            
        print(tempNode.data)
