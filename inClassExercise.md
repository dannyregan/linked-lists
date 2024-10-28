```python

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
    
    def printList(self,msg = '----'):
        p = self.header
        print("----",msg)
        while (p is not None):
            print(p.data, end=' ')
            p = p.next
        if (self.current is not None):
            print("Currrent:", self.current.data)
        else:
            print("Empty linked list")
        input("=======================")


def main():
    mylist = LinkedList()
    mylist.printList("List created")
    mylist.insertBeginning(76)
    mylist.insertBeginning(88)
    mylist.insertBeginning(11)
    mylist.insertBeginning(34)
    mylist.insertBeginning(56)
    mylist.insertBeginning(91)
    mylist.printList("Inserting numbers")
    mylist.nextCurrent()
    mylist.nextCurrent()
    mylist.nextCurrent()
    mylist.printList("Pushing current to third element in the list")
    mylist.removeCurrentNext()
    mylist.printList("Removing the next element")
    mylist.insertCurrentNext(23)
    mylist.printList("Adding 23 next to current")

# ===========================================

main()

# ===========================================

# OUTPUT
---- List created
Empty linked list
---- Inserting numbers
91 56 34 11 88 76 Currrent: 76
---- Pushing current to third element in the list
91 56 34 11 88 76 Currrent: 34
---- Removing the next element
91 56 34 88 76 Currrent: 34
---- Adding 23 next to current
91 56 34 23 88 76 Currrent: 34
```