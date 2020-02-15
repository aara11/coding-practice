m=int(input())
for j in range(1,m+1):
    n=int(input())
    arr=input().strip().split()
    arr=[int(x) for x in arr]
    arr=sorted(arr)
    err=0
    for i in range(int(n/2)):
        err+=(i-arr[2*i])**2
        err+=(i-arr[2*i+1])**2
    if n%2==1:
        err+=(arr[-1]-int(n/2))**2
    print('Case #'+str(j)+': '+str(err))