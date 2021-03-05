class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.initialize()

    # 리스트 비우기
    def initialize(self):
        self.__head = None

    # Node 추가
    def addNode(self, data):
        newNode = Node(data)

        if not self.isEmpty():
            tempNode = self.__head

            while tempNode.next:
                tempNode = tempNode.next

            tempNode.next = newNode

        self.__head = newNode

    # index번째에 Node 삽입
    def insertNode(self, index ,data):
        if index > self.getListSize() or index < 0:
            return -1
        
        tempNode = self.__head
        prevNode = None

        for _ in range(index):
            prevNode = tempNode
            tempNode = tempNode.next

        newNode  = Node(data)
        prevNode.next = newNode
        newNode.next = tempNode

    # index번째에 Node data 수정
    def updateNode(self, index, data):
        if index > self.getListSize() or index < 0:
            return -1
        
        tempNode = self.__head

        for _ in range(index):
            tempNode = tempNode.next

        tempNode.data = data

    # data값을 가진 Node 1개 삭제
    def deleteNodeData(self, data):
        if self.isEmpty():
            return -1

        tempNode = self.__head
        prevNode = None

        if tempNode.data == data:
            self.__head = tempNode.next
            tempNode = None
            return

        while tempNode:
            if tempNode.data == data:
                prevNode.next = tempNode.next
                return
            
            prevNode = tempNode
            tempNode = tempNode.next
            
        return -1

    # index번째에 Node 삭제
    def deleteNodeIndex(self, index):
        if index + 1 > self.getListSize() or index < 0:
            return -1

        tempNode = self.__head
        prevNode = None

        if index:
            for _ in range(index):
                prevNode = tempNode
                tempNode = tempNode.next

            prevNode.next = tempNode.next
            return

        self.__head = tempNode.next

    # index번째에 Node data 반환
    def getNodeData(self, index):
        if index > self.getListSize() or index < 0:
            return -1
        
        tempNode = self.__head
        
        for _ in range(index):
            tempNode = tempNode.next

        return tempNode.data

    # 사이즈 반환
    def getListSize(self):
        size = 0
        tempNode = self.__head

        while tempNode:
            size += 1
            tempNode = tempNode.next

        return size
    
    # 비어있는지 확인
    def isEmpty(self):
        return not self.getListSize()

    # 전체 출력
    def printAll(self):
        idx = 0
        tempNode = self.__head

        while tempNode:
            idx +=  1
            print(tempNode.data)
            tempNode = tempNode.next