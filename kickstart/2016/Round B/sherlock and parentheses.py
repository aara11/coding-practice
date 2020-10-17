t = int(input())
for tt in range(1, t + 1):
    l,r = [int(x) for x in input().strip().split()]
    ans = l
    if r<l:
        ans=r
    ans=ans*(ans+1)/2
    print("Case #" + str(tt) + ": " + str(int(ans)))