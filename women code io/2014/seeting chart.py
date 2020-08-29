fact={}
fact[0]=1
lim=0
def get(val):
    global lim
    if val<=lim:
        return fact[val]
    for i in range(lim+1,val+1):
        fact[i]=i*fact[i-1]
    lim=val
    return fact[val]

t=int(input())

for tt in range(1,t+1):
    n,k=[int(x) for x in input().strip().split()]
    min_=n//k
    rem=n%k
    den=get(rem)*get(k-rem)
    if min_==2:
        den=den*(pow(2,k-rem))
    elif min_>2:
        den=den*(pow(2*min_,k-rem))
    if rem>0:
        if min_+1==2:
            den=den*(pow(2,rem))
        elif min_+1>2:
            den=den*(pow(2*(min_+1),rem))
    num=get(n)
    ans=num/den
    print("Case #"+str(tt)+": "+str(int(ans)))
