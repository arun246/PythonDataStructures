def power(x,n):
    if n== 0:
        return 1
    else:
        first=power(x,n//2)
        res= first*first
        if (n%2==1):
            return x*res
        return res

print(power(2,3))
