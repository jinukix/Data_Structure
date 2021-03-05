
TABLE_SIZE = 10

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.hashNext = None

class HashMap:
    def __init__(self):
        self.initialize()

    def initialize(self):
        self.__table = [None for _ in range(TABLE_SIZE)]

    def add(self, key, value):
        newNode = Node(key, value)
        # hash의 key값은 int형으로 받아 10으로 나눈 나머지값으로 처리 
        hash = key % TABLE_SIZE

        if not self.__table[hash]:
            self.__table[hash] = newNode
            return
        
        entry = self.__table[hash]

        while (entry.hashNext) and (entry.key != key):
            entry = entry.hashNext

        # 같은 key값이 존재하는 경우 덮어쓰기.
        if entry.key == key:
            entry.data = value
            return
        
        entry.hashNext = newNode

    def getValue(self, key):
        hash = key % TABLE_SIZE
        entry = self.__table[hash]

        while (entry.hashNext) and (entry.key != key):
            entry = entry.hashNext

        if entry.key == key:
            return entry.data

        return -1        

    def remove(self, key):
        hash = key % TABLE_SIZE

        if not self.__table[hash]:
            return -1

        if self.__table[hash].key == key:
            self.__table[hash] = None

        entry = self.__table[hash]
        temp = entry.hashNext

        while (entry.hashNext) and (temp.key != key):
            entry = entry.hashNext
            temp = entry.hashNext

        if temp.key == key:
            entry.hashNext = temp.hashNext
            return

        return -1

    # 해당 key값 데이터 출력
    def printKey(self, key):
        hash = key % TABLE_SIZE
        entry = self.__table[hash]

        while entry.hashNext:
            print(entry.data)
            entry = entry.hashNext

        print(entry.data)