from operator import attrgetter
class GameScore:

    def __init__(self,name,score):
        self._name= name
        self._score= score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return 'name {0}, score {1}' .format(self._name, self._score)

class ScoreBoard:
    
    def __init__(self,n=5):
        self._capacity = n
        self._board = [None]*self._capacity
        self._num = 0

    def __get_item__(self,k):
        return self._board[k]

    def __str__(self):
        strr = "\n game score \n"
        strr2= "\n".join(str(self._board[j]) for j in range(self._num))
        strr3=strr+strr2
        return strr3
        ##return 'Game scoreboard \n {}'.format(self._board[k] for k in range(self._num))

    def add(self,newscore):
        nn= newscore.get_name()
        ns = newscore.get_score()

        f_row = self._board[0].get_score()
        l_row = self._board[self._num-1].get_score()
        ##scoreboard is empty
        if(self._num == 0):
            self._scoreboard[0]._score = ns
            self._socreboard[0]._name = nn
            self._num += 1
        ##if scoreboard is filled but less than capacity
        if((self._num >= 1) and (self._num < self._capacity)):
            #adding score at 
            if(self._num ==  1):
                self._board[self._num] = ns
                self._num +=1 
            ##adding new score at last #self._num 2
            if(self._num >1):
                if(ns > l_row):
                    self._board[self._num] = ns
                    self._board[self._num] = nn
                    self._num += 1
                if(ns < l_row):
                    self._board[self._num] = ns
                    self._board[self._num] = nn
                    self._num += 1
                    
      
        ##if scoreboard is full
        if(self._num == self._capacity)
            ##if score is more than high score
            if ( ns >= l_row ):
                for j in range(0,self._num):#0-4
                    if(j == self._num-1 ):
                        break
                    self._board[j] = self._board[j+1]
                self._board[self._num-1]._score=ns
                self._board[self._num-1]._name=nn
                return True

            ##if score is between curr high and low score
            elif((ns >= f_row) and (ns < l_row) ):
                for i in range(self._num-1,-1,-1):##3-0
                    if (ns > self._board[i].get_score()):##2
                        ##print("hello i",i)
                        for j in range(0,i):##0-1
                            ##print("hello j",j)
                            self._board[j] = self._board[j+1]
                        self._board[i]._score = ns
                        self._board[i]._name=nn
                        return True
                    continue
                
 ## Testing Area
scoBoard= ScoreBoard(5)
print("scoreboard with capacity 5 created\n")
print("please add 3 scores")
for i in range(5):
    print("score num",i)
    scoBoard._board[i] = GameScore("hell"+str(i),int(input("Enter a score")))
    scoBoard._num += 1 

print(scoBoard)
sorted(scoBoard._board, key=attrgetter('_score'))

print(scoBoard.add(GameScore("hell5",400)))

print(scoBoard)

