class Simp_stack:

    def __init__(self):
        self._mem = []
        self._num = 0

    def _len(self):
        return self._num

    def push(self,ele):
        self._mem.append(ele)
        self._num += 1 


    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        self._num -= 1
        return self._mem.pop()

    def is_empty(self):
        if(self._num == 0):
            return True
        return False
        
def reverse_file(filename):
    print("start")
    file = open(filename,"r+")
    s=Simp_stack()
    for line in file:
        s.push(line)
    file.close()
    print(s._mem)

    o_file = open("out.txt","w+")
    while(not s.is_empty()):
        o_file.write(s.pop()+"\n")
    o_file.close()
    return True

s=Simp_stack()
s.push("hello")
s.push("there")

print(s._mem)
print(reverse_file("myfile.txt"))
print("finished")
    

    
