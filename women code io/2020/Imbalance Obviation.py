t=int(input().strip())
def opp(val):
    lst=["L","R"]
    lst.remove(val)
    return lst[0]
    
for tt in range(1,t+1):
    n=int(input().strip())
    arr=input().strip().split()
    arr=[int(x)-1 for x in arr]
    arr.reverse()
    place={}
    for i in range(n):
        place[arr[i]]=i# maps out order for a index
    
    ans = ["" for i in range(n)]
    for i in range(n-1,-1,-1):
        if ans[arr[i]]=="":
            ans[arr[i]]="L"
            lst=[arr[i]]
            if i%2==0 and i+1<n:
                ans[arr[i+1]]="R"
                lst.append(arr[i+1])
            elif i%2==1:
                ans[arr[i-1]]="R"
                lst.append(arr[i-1])
                #lst-> marbles whihc we have to check
            while(len(lst))>0:
                val=lst[0]
                lst=lst[1:]
                if val%2==0 and val+1<n:
                    ans[val+1]=opp(ans[val])
                    neg = val+1
                elif val%2==1:
                    ans[val-1]=opp(ans[val])
                    neg = val-1
                else:
                    continue
                handle = place[neg]
                if handle%2==0 and handle+1<n:
                    if ans[arr[handle+1]]=="":
                        ans[arr[handle+1]]=opp(ans[neg])
                        lst.append(arr[handle+1])
                elif handle%2==1:
                    if ans[arr[handle-1]]=="":
                        ans[arr[handle-1]]=opp(ans[neg])
                        lst.append(arr[handle-1])
    print("Case #"+str(tt)+": "+"".join(ans))

