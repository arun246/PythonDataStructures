def reverse(seq,f,l):
    if f < l-1:
        seq[f],seq[l-1]=seq[l-1],seq[f]
        reverse(seq,f+1,l-1)
seq=[1,2,3,4,5,6,7,8,9]
reverse(seq,0,9)
print(seq)
