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

def html_tags(html):
    s = Simp_stack()
    j = html.find('<')
    while(j != -1):
        print("j",j)
        k = html.find('>',j+1)
        print("k",k)
        if(k==-1):
            return False
        tag = html[j+1:k]
        if(not tag.startswith('/')):
            s.push(tag)
        else:
            if(s.is_empty()):
                return False
            if (tag[1:] != s.pop()):
                return False
        j = html.find("<",k+1)
    return "success"   
        
            


html = "<body><center><h1> The Little Boat </h1></center><p> The storm tossedthe littleboat like a cheap sneaker in anold washing machine. Thethreedrunken fishermen were used tosuch treatment, of course, butnot thetree salesman, who even asa stowaway now felt that hehad overpaid forthe voyage. </p><ol><li> Will the salesman die? </li><li> What color isthe boat? </li><li> And what about Naomi? </li></ol></body>"

print(html_tags(html))
