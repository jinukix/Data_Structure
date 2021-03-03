class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:

    """
    Linked List는 배열처럼 순서가 있는 자료구조입니다.
    하지만 배열과는 여러 면에서 차이를 보입니다.

    Linked List는 배열처럼 index가 있는것이 아니고 각 요소들이 다음 요소들을 가리키는 형식으로 되어 있습니다.
    그렇다 보니 배열처럼 원하는 index에 접근해 바로 값을 가지고오는 것이 불가능합니다.
    Linked List에서 원하는 값을 가지고오려면 무조건 첫 번째 요소부터 순서대로 확인해야 합니다.
    """
    
    def __init__(self):
        self.clearAllNode()

    def addNode(self, data):
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            tempNode = self.head

            while tempNode.next:
                tempNode = tempNode.next
            tempNode.next = newNode

    def insertNode(self, index ,data):
        if not self.head or index > self.getListSize():
            return
        
        newNode  = Node(data)
        tempNode = self.head
        prevNode = None

        idx = 0

        while tempNode:
            if idx == index:
                if tempNode == self.head:
                    self.head = newNode
                else:
                    prevNode.next = newNode
                
                newNode.next = tempNode
                break
            else:
                prevNode = tempNode
                tempNode = tempNode.next
                idx+=1

    def updateNode(self, index, data):
        if not self.head or index > self.getListSize():
            return
        
        tempNode = self.head
        idx = 0 

        while tempNode:
            if idx == index:
                tempNode.data = data
                return
            else:
                idx+=1
                tempNode = tempNode.next

    def deleteNodeData(self, data):
        if not self.head:
            return

        tempNode = self.head
        prevNode = None

        while tempNode:
            if tempNode.data == data:
                if tempNode == self.head:
                    self.head = tempNode.next
                else:
                    prevNode.next = tempNode.next
                
                tempNode = None
                return
            
            prevNode = tempNode
            tempNode = tempNode.next

    def deleteNodeIndex(self, index):
        if not self.head or index > self.getListSize():
            return

        tempNode = self.head
        prevNode = None
        idx = 0

        while tempNode:
            if idx == index:
                if tempNode == self.head:
                    self.head = tempNode.next
                else:
                    prevNode.next = tempNode.next

                tempNode = None
                return

            idx+=1
            prevNode = tempNode
            tempNode = tempNode.next


    def clearAllNode(self):
        self.head = None

    def getNodeData(self, index):
        if not self.head or index > self.getListSize():
            return
        
        tempNode = self.head
        idx = 0 

        while tempNode:
            if idx == index:
                return tempNode.data
            else:
                idx+=1
                tempNode = tempNode.next

    def getListSize(self):
        idx = 0

        if self.head:
            tempNode = self.head

            while tempNode:
                idx +=  1
                tempNode = tempNode.next

        return idx
        
    def isEmpty(self):
        return not self.getListSize()

    def printAll(self):
        if self.head:
            idx = 0
            tempNode = self.head

            while tempNode:
                idx +=  1
                print(tempNode.data)
                tempNode = tempNode.next