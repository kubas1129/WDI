class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class UnidirectionalList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        if not self.head:
            n = Node(data)
            self.head = n
        else:
            n = self.head
            while n.next != None:
                n = n.next
            new_node = Node(data)
            n.next = new_node;

    def printList(self):
        n = self.head
        while n:
            print(n)
            n = n.next



class Node2:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)


class TwoDirectionalList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addOnTail(self, data):
        if(self.head == None):
            new = Node2(data)
            self.head = new
        else:
            n = self.head
            while n.next != None:
                n = n.next
            new = Node2(data)
            n.next = new

    def addOnBegin(self,data):
        if(self.head == None):
            new = Node2(data)
            self.head = new
        else:
            new = Node2(data)
            new.next = self.head
            self.head.prev = new
            self.head = new


    def insert(self,data,index):
        if(self.head == None):
            new = Node2(data)
            self.head = new
        else:
            n = self.head
            i = 1
            while(i < index-1):
                if(n.next == None):
                    self.addOnTail(data)
                    return
                n = n.next
                i += 1
            new = Node2(data)
            new.next = n.next
            n.next.prev = new
            n.next = new
            new.prev = n


    def printList(self):
        n = self.head
        while n:
            print(n)
            n = n.next





ll = TwoDirectionalList()
ll.addOnTail(14)
ll.addOnTail("test")
ll.addOnTail(2.34)
ll.addOnTail(True)
ll.insert(5,6)
ll.addOnBegin("NaPoczatku")

ll.printList()