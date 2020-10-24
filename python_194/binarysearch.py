def binarysearch(data,target,low,high):


    mid=(low+high)//2
    term=data[mid]
    if(term == target):
        return "found at"+str(mid)
    elif(data[mid] == None):
        return "fund null at"+str(mid)
    elif (data[mid] > target):
        return binarysearch(data,target,low,mid-1)
    else:
        return binarysearch(data,target,mid+1,high)
a=[1,2,3,4,5,None,7,8]
print(binarysearch(a,None,0,len(a)))      
