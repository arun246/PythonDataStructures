alp= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
msg=['a','b','c','d','e','f']
print(''.join(msg))

r=int(input(" enter a number as key"))
for i in range(len(msg)):
    rep = (i+r)%26
    msg[i]= alp[rep]

print(''.join(msg))


    
