## resizable and garbage collection based queue (FIFO)
#this is queue with a circular structure
class MyQueue:

    def __init__(self,capacity):
        self._arr = [None]*capacity
        self._e_num = 0
        self._f = 0

    def __len__(self):
        return self._e_num

    def enqueue(self,ele):
        if (self._e_num == len(self._arr)):
            self.resize(2*len(self._arr))
        new_i = (self._f + self._e_num)%len(self._arr) ##insertion with wrap through
        self._arr[new_i] = ele
        self._e_num += 1

    def dequeue(self,ele):
        if (self.is_empty()):
            return False
        ans = self._arr[self._f]
        self._arr[self._f] = None
        self._f = (self._f + 1)%len(self._arr)
        self._e_num -= 1
        return ans

    def first(self):
        return self._arr[self._f]

    def __str__(self):
        str1 =  " ".join(str(self._arr[i]) for i in range(len(self._arr)))
        return str1 

    def is_empty(self):
        if(self.num == 0):
            return True

    def resize(self,new_s):
        old = self._arr
        self._arr = [None]*new_s
        new_f = self._f
        for i in range(len(old)):
            self._arr[i] = old[new_f]
            new_f = (new_f+1)%len(old)
            self._f = 0
        return self._arr

    ##testing area

q = MyQueue()
q.enqueue(1)
print(q)
