t=int(input())
for i in range(1,t+1):
    x=input().strip().split()
    d=int(x[0])
    p=int(x[1])
    l=d
    aI=['I']*l
    a_=['/']*l
    aO=['O']*l
    maxx=3*(l-2)+2
    final=[]
    rem=int(p%maxx)
    q=int(p/maxx)
    final.append(''.join(aI))
#    print(maxx,rem,q)
    for j in range(int(q)):
        final.append(''.join(a_))
        if j%2==0:
            final.append(''.join(aO))
        else:
            final.append(''.join(aI))
#    print(final,a_)
    if rem>0:
        missing=maxx-rem
#        print(missing)
        if missing>=3:
            num=int(missing/3)
#            print('num = ',num)
            for j in range(1,num+1):
                a_[j]='O'
#            print(missing)
            missing-=(num*3)
        if missing>=1:
            a_[0]='O'
            missing -=1
        if missing>=1:
            a_[l-1]='O'
        final.append(''.join(a_))
        if q%2==0:
            final.append(''.join(aO))
        else:
            final.append(''.join(aI))
    ans=[]
    for f in final:
        ans.append(f)
        ans.append('\n')
    ans=ans[:-1]
    ans=''.join(ans)
    print('Case #'+str(i)+':')
    print(ans)