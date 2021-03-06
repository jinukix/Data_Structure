class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Graph:
    def __init__(self):
        self.__graph = None

    # 트리 초기화
    def initializeGraph(self, graphCount):
        self.__graph = [None for _ in range(graphCount)]

    # 그래프 연결 start -> end
    def addEdge(self, start, end):
        newNode = Node(end)

        if not self.__graph[start]:
            self.__graph[start] = newNode
        else:
            newNode.next = self.__graph[start]
            self.__graph[start] = newNode

    # 연결 해제 start->end
    def deleteEdge(self, start, end):
        if not self.__graph[start]:
            return -1

        temp = self.__graph[start]
        prev = None

        while temp.next and temp.data != end:
            prev = temp
            temp = temp.next

        if temp.data == end:
            if not prev:
                self.__graph[start] = temp.next
            else:
                prev.next = temp.next
            return

        return -1

    # edge에 연결된 그래프 출력.
    def showGraphEdge(self, edge):
        if self.__graph[edge]:
            temp = self.__graph[edge]

            while temp:
                print(f"{edge} => {temp.data}")
                temp = temp.next