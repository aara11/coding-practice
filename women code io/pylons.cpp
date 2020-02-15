t=int(input())
for tt in range(1,t+1):
    r,c=[int(x) for x in input().strip().split()]
    max_=max(r,c)
    if max_<=3:
        print("Case #"+str(tt)+": IMPOSSIBLE")
        continue
    rev=0
    ans=[]
    if r>c:
        rev=1
        p=r
        r=c
        c=p
    if r==2:
        if c<=4:
            print("Case #"+str(tt)+": IMPOSSIBLE")
            continue
        j=3
        for i in range(c):
            ans.append([0,i])
            ans.append([1,(i+j)%c])
    else:
        j=2
        for i in range(c):
            if i==c-1 and r==c and r%2==0:
                for k in range(1,r):
                    if k%2==0:
                        ans.append([k,i])
                    else:
                        ans.append([k,(i+j)%c])
                ans.append([0,i])
                continue

            for k in range(r):
                if k%2==0:
                    ans.append([k,i])
                else:
                    ans.append([k,(i+j)%c])
    
    out=[]
    if rev:
        for l in ans:
            out.append([l[1]+1,l[0]+1])
    else:
        for l in ans:
            out.append([l[0]+1,l[1]+1])
    
    print("Case #"+str(tt)+": POSSIBLE")
    for l in out:
        print(str(l[0])+" "+str(l[1]))
    #for i in range(len(out)-1):
     #   val=abs(out[i][0]-out[i+1][0])
      #  val1=abs(out[i][1]-out[i+1][1])
       # if val==val1:
        #    print("fdjvbf",out[i])
    
    