def binary_search_norecur(seq,search,f,l):
    
    while(f <= l):
        mid = (f+l)//2
        if (search == seq[mid]):
            return "target found at "+str(mid)
        elif search < seq[mid]:
            l = mid-1
        else:
            f= mid+1
    return "not found"

a=[1,2,3,4,5,6,7,8,9,10]
print(binary_search_norecur(a,5,0,len(a)-1))
        
    
