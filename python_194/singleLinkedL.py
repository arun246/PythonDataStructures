class Node:

    def __init__(self):
        self._ele = None
        self._next = None

class SLinkedList:

    def __init__(self):
        self._head = Node()
        self._num = 0
        self._tail = self._head

    def add(self,ele):
        if(self._num <= 1):
            self._tail = self._head._next
        curr = self._head
        self._head = Node()
        self._head._ele = ele
        self._head._next = curr
        self._num += 1

    def first(self):##first Node
        return self._head

    def last(self):##last Node
        return self._tail

## Testing Area

sl = SLinkedList()
sl.add(5)
print(sl.first()._ele)
print(sl.last() == None)
sl.add(6)
print(sl.first()._ele)

    
    
        
