def sums(seq,n):
    if n == 0:
        return 0
    else:
        return sums(seq,n-1)+seq[n-1]


print(sums([1,2,3,4,5,6,7,8,9,10],10))
