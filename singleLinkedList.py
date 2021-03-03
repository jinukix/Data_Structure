class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.__head = None

    # Node 추가
    def addNode(self, data):
        newNode = Node(data)

        if self.__head:
            tempNode = self.__head

            while tempNode.next:
                tempNode = tempNode.next
            tempNode.next = newNode
            return

        self.__head = newNode

    # index번째에 Node 삽입
    def insertNode(self, index ,data):
        if index > self.getListSize() or index < 0:
            return
        
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
            return
        
        tempNode = self.__head

        for _ in range(index):
            tempNode = tempNode.next

        tempNode.data = data

    # data값을 가진 Node 1개 삭제
    def deleteNodeData(self, data):
        if not self.__head:
            return

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

    # index번째에 Node 삭제
    def deleteNodeIndex(self, index):
        if index > self.getListSize() or index < 0:
            return

        tempNode = self.__head
        prevNode = None

        if not index:
            self.__head = tempNode.next
            return

        for _ in range(index):
            prevNode = tempNode
            tempNode = tempNode.next

        if tempNode == self.__head:
            prevNode.next = tempNode.next

    # 리스트 비우기
    def clear(self):
        self.__head = None

    # index번째에 Node data 반환
    def getNodeData(self, index):
        if index > self.getListSize() or index < 0:
            return
        
        tempNode = self.__head
        
        for _ in range(index):
            tempNode = tempNode.next

        return tempNode.data

    # 리스트 길이
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