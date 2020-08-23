poss=[]
diff=-1
def add(d):
    global diff
    if d==0:
        poss.append(1)
        diff=0
        return
    val=6+(6*(d-1))
    poss.append(val)
    diff=d
    
t=int(input())
for tt in range(1,t+1):
    ans=0
    k,v=[int(x) for x in input().strip().split()]
    for d in range(v+1):
        if d>diff:
            add(d)
        ans+=poss[d]*(k-d+1)
    
    print("Case #"+str(tt)+": "+str(ans))