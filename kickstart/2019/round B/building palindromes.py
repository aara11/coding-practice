t=int(input().strip())
for i in range(1,t+1):
    ans=0
    n,q=map(int,input().strip().split())
    arr=input().strip()
    mp=[0 for i in range(26)]
    lst=[]
    lst.append(mp[:])
    for k in range(n):
        idx=ord(arr[k])-ord('A')
        mp[idx]+=1
        lst.append(mp[:])
    for k in range(q):
        l,r=map(int,input().strip().split())
        summ=0
        for j in range(26):
            if (lst[r][j]-lst[l-1][j])%2==1:
                summ+=1
            if summ>1:
                break
        if summ<=1:
            ans+=1
    print("Case #"+str(i)+": "+str(ans))