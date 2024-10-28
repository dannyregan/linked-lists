class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class LinkedList:
    def __init__(self, d = None):
        if (d == None):
            self.header = None
            self.current = None
        else:
            self.header = Node(d)
            self.current = self.header
        
    def insertBeginning(self, d):
        if (self.header is None):
            self.header = Node(d)
            self.current = self.header
        else:
            tmp = Node(d)
            tmp.next = self.header
            self.header = tmp
    
    def insertCurrentNext(self, d):
        if (self.header is None):
            self.header = Node(d)
            self.current = self.header
        else:
            tmp = Node(d)
            tmp.next = self.current.next
            self.current.next = tmp
    
    def removeBeginning(self):
        if (self.header is None):
            return None
        else:
            ans = self.header.data
            self.header = self.header.next
            self.current = self.header
            return ans
        
    def removeCurrentNext(self):
        if (self.header is None):
            return None
        else:
            ans = self.current.next.data
            self.current.next = self.current.next.next
            return ans
        
    def nextCurrent(self):
        if (self.current.next is not None):
            self.current = self.current.next
        else:
            self.current = self.header
        
    def resetCurrent(self):
        self.current = self.header

    def getCurrent(self):
        if (self.current is not None):
            return self.current.data
        else:
            return None
    
    def printList(self,msg = '========'):
        p = self.header
        print("======",msg)
        while (p is not None):
            print(p.data, end=' ')
            p = p.next
        if (self.current is not None):
            print("Currrent:", self.current.data)
        else:
            print("Empty linked list")
        input("--------------")


def main():
    mylist = LinkedList()
    mylist.printList("List created")
    mylist.insertBeginning(40)
    mylist.printList("Inserting 40 at Beginning")
    mylist.insertBeginning(20)
    mylist.printList("Inserting 20 at Beginning")
    mylist.nextCurrent()
    mylist.printList("Moving the Current to the next (circularly)")
    print("The current is:", mylist.getCurrent())
    mylist.insertCurrentNext(30)
    mylist.printList("Inserting 30 next the Current")
    mylist.nextCurrent()
    mylist.printList("Moving the Current to the next")
    print("The current is:", mylist.getCurrent())
    mylist.resetCurrent()
    mylist.printList("Reseting the Current")
    mylist.insertCurrentNext(25)
    mylist.printList("Inserting 25 next to the Current")
    print(mylist.removeBeginning())
    mylist.printList("Removing at the Beginning")
    print(mylist.removeCurrentNext())
    mylist.printList("Removing next the Current")
    print("Now, do it again just to be sure you've got it!")

# ===========================================

main()