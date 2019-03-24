def Fabfun(n):
    l=[1,1]
    for i in range(n-2):
        l.append(l[-1]+l[-2])
    return l

#print Fabfun(10)
