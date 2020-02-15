t=int(input().strip())

for tt in range(1,t+1):
    arr=input().strip()
    l=len(arr)
    dic={}
    ans=0
    for i in range(l):
        if arr[i]=="I" or arr[i]=="i":
            if arr[i] not in dic:
                dic[arr[i]]=0
            dic[arr[i]]+=1
        else:
            if arr[i]=="O":
                if "I" in dic:
                    if dic["I"]>0:
                        ans+=1
                        dic["I"]-=1
                        continue
            if "i" in dic:
                if dic["i"]>0:
                    dic["i"]-=1
                    continue
            dic["I"]-=1
            
    print("Case #"+str(tt)+": "+str(ans))

