
t=int(input())
for tt in range(1,t+1):
    n=int(input())
    xx=input().strip().split()
    m=[int(x) for x in xx]
    st=0
    val=m[0]
    ct=0
    min_=1001
    max_=-1
    for i in range(1,n+1):
        if m[i]>min_ and val>min_:
            st=i
            val=m[i]
            ct+=1
            min_=1001
            max_=-1
            continue
        elif m[i]<max_ and val<max_:
            st=i
            val=m[i]
            ct+=1
            min_=1001
            max_=-1
            continue
        max_=max(max_,m[i])
        min_=min(min_,m[i])
    print('Case #'+str(tt)+': '+str(ct-1))