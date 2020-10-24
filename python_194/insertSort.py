a=[3,2,4,1,5]
def insertionsort(A):
    for i in range(1,len(A)):#1,4
        curr = A[i]
        for j in range(i,0,-1):#1
            if(curr < A[j-1]):
                A[j-1],A[j]=A[j],A[j-1]
                
    return "success"

print(insertionsort(a))
print(a)
