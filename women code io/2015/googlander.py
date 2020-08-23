poss={}
def get(r,c):
    if (r,c) in possa
        return poss[(r,c)]
    if r==1 or c==1:
        poss[(r,c)]=1
        return 1
    val=0
    for i in range(1,r+1):
        val+=get(c-1,i)
    poss[(r,c)]=val
    return val


t=int(input())
for tt in range(1,t+1):
    r,c=[int(x) for x in input().strip().split()]
    ans=get(r,c)
    print("Case #"+str(tt)+": "+str(ans))