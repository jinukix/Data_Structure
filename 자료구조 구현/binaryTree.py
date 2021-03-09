class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.initialize()

    # 트리 초기화
    def initialize(self):
        self.__root = None

    # Node 추가
    def addNode(self, data):
        newNode = Node(data)
        root = self.__root

        if not root:
            self.__root = newNode
        else:
            self.__insertNode(root, newNode)

    # Node 삭제
    def removeNode(self, data):
        if not self.__root:
            return -1

        self.__deleteNode(self.__root, data)

    # 전체 출력
    def printAll(self):
        self.__inOrder(self.__root);

    """ 내부 구현 용도 함수 (재귀) """

    # Node 삽입
    def __insertNode(self, root, newNode):
        if root.data < newNode.data:
            if not root.right:
                root.right = newNode
            else:
                self.__insertNode(root.right, newNode)
        elif root.data > newNode.data:
            if not root.left:
                root.left = newNode
            else:
                self.__insertNode(root.left, newNode)

    # Node 삭제
    def __deleteNode(self, root, data):
        if not root:
            return None
        elif data < root.data:
            root.left = self.__deleteNode(root.left, data)
        elif data > root.data:
            root.right = self.__deleteNode(root.right, data)
        else:
            # 자식이 없는 경우
            if not root.left and not root.right:
                if root == self.__root:
                    self.__root = None
                else:
                    root = None
            # 자식이 오른쪽에 하나
            elif not root.left:
                if root == self.__root:
                    self.__root = root.right
                else:
                    root = root.right
            # 자식이 왼쪽에 하나
            elif not root.right:
                if root == self.__root:
                    self.__root = root.left
                else:
                    root = root.left
            # 자식이 양쪽에 있을 때
            else:
                minNode = self.__findMin(root.right)
                root.data = minNode.data
                root.right = self.__deleteNode(root.right, minNode.data)

        return root
        
    # 최저값 찾기
    def __findMin(self, root):
        while root.left:
            root = root.left

        return root

    # 작은값부터 호출
    def __inOrder(self, root):
        if not root:
            return

        self.__inOrder(root.left)
        print(root.data)
        self.__inOrder(root.right)
