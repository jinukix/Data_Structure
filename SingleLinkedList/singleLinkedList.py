class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
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