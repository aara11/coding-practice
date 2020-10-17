def get_intervals(l1,r1,a,b,c1,c2,m,n):
    intervals=[[l1,r1]]
    x1=l1
    y1=r1
    for i in range(n-1):
        x2=(a*x1+b*y1+c1)%m
        y2=(a*y1+b*x1+c2)%m
        x1=min(x2,y2)
        y1=max(x2,y2)
        intervals.append([x1,y1])
        x1,y1=x2,y2
    return intervals

def add_interval(interval, end,path):
    if end<interval[0]:
        path+=1
    start_new=max(interval[0],end)
    end_new=max(interval[1],end)
    return (end_new, path+end_new-start_new)

t = int(input())
for tt in range(1,t+1):
    n,l1,r1,a,b,c1,c2,m=[int(x) for x in input().strip().split()]
    intervals=get_intervals(l1,r1,a,b,c1,c2,m,n)
    intervals=sorted(intervals)
    comp=(-1,0)
    mp={}
    for i in range(n):
        comp_new=add_interval(intervals[i],comp[0], comp[1])
        mp_={}
        for k,v in mp.items():
            end,tot=add_interval(intervals[i],k,v)
            if end not in mp_:
                mp_[end]=tot
            elif mp_[end]>tot:
                mp_[end]=tot
        if comp[0] not in mp_:
            mp_[comp[0]]=comp[1]
        elif mp_[comp[0]]>comp[1]:
            mp_[comp[0]]=comp[1]
        mp=mp_.copy()
        comp=comp_new
    ans=sorted(list(mp.values()))[0]
    print("Case #"+str(tt)+": "+str(ans))