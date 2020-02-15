t=int(input())
for i in range(1,1+t):
    n=int(input())
    x=input()
    aa=[int(p) for p in x]
    v=len(aa)
    w=(v+1)//2
    sum_=0
    for k in range(w):
        sum_+=aa[k]
    max_=sum_
    for k in range(w,v):
        sum_=sum_+aa[k]-aa[k-w]
        max_=max(max_,sum_)
    print('Case #'+str(i)+': '+str(max_))