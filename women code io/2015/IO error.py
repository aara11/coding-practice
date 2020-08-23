def strtobinary(s):
    if len(s)==0:
        return 0
    if len(s)==1:
        if s=="I":
            return 1
        else:
            return 0
        
    val=2*strtobinary(s[:-1])
    if s[-1]=="I":
        return val+1
    return val

t=int(input())
for i in range(1,t+1):
    b=int(input())
    arr=input()
    ans=""
    for j in range(b):
        st=arr[:8]
        arr=arr[8:]
        val=strtobinary(st)
        ans+=chr(val)
    
    print("Case #"+str(i)+": "+ans)
    