def puzzlesolve(num,seq,set_seq):
    for i in range(len(set_seq)) :
        seq.append(set_seq.pop(0))
        if num == 1:
            if len(seq)== num:
                print( seq)
        else:
            puzzlesolve(num-1,seq,set_seq)
        set_seq.append(seq.pop(0))


print(puzzlesolve(3,[],['a','b','c']))
