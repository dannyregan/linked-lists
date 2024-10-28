__author__ = "Danny Regan"

class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.prev = None

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
            tmp.prev = self.current
            self.current.next = tmp
        
    def insertCurrentPrev(self, d):
        if (self.header is None):
            self.header = Node(d)
            self.current = self.header
        if (self.current == self.header):
            self.insertBeginning(d)
        if (self.current.prev):
            tmp = Node(d)
            tmp.next = self.current
            tmp.prev = self.current.prev.prev
            self.current.prev.prev.next = tmp
            self.current.prev = tmp
    
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
        
    def removeCurrent(self):
        if (self.header is None):
            return None
        if (self.current == self.header):
            return self.removeBeginning()
        if (self.current.next):
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
        else:
            self.current.prev.next = None
        if (self.current.next):
            self.current = self.current.next
        else:
            self.current = self.header
        return None
        
    def nextCurrent(self):
        if (self.current.next is not None):
            self.current = self.current.next
        else:
            self.current = self.header
        
    def resetCurrent(self):
        self.current = self.header
        return self.header

    def getCurrent(self):
        if (self.current is not None):
            return self.current.data
        else:
            return None

    def printList(self):
        p = self.header
        print("=====================================================================")
        while (p is not None):
            print(p.data, end=' ')
            p = p.next
        if (self.current is not None):
            print("Currrent:", self.current.data)
        else:
            print("Empty linked list")
        print("=====================================================================")

def main():
    with open('data.txt', 'r') as file:
        a = [int(line) for line in file]
        a.sort()
        L = LinkedList()
        for num in a:
            L.insertCurrentNext(num)
            L.nextCurrent()
        L.resetCurrent()

    while True:
        L.printList()
        x = int(input("Input an integer value, or 0 to EXIT: "))
        if x in a:
            L.resetCurrent()
            while L.current.data != x:
                L.nextCurrent()
            L.removeCurrent()
            a.remove(x)
        elif x not in a and x != 0:
            L.resetCurrent()
            while L.current.next is not None and x > L.current.data:
                L.nextCurrent()
            if x > L.current.data:
                L.insertCurrentNext(x)
            else:
                L.insertCurrentPrev(x)
            a.append(x)
            a.sort()
        
        elif x == 0:
            break

# ========================================
main()