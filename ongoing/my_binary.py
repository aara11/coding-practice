import sys

t,n=[int(x) for x in input().strip().split(" ")]
for _ in range(t):
    out="AAAAA"
    i=0
    reached=false
    print(out)
    sys.stdout.flush()
    first=""
    last=""
    while(i<25):
        s1=input().strip()
        if first !="":
            if s1==last:
                print(first)
            else:
                print(last)
        else:
            print(out)
        sys.stdout.flush()
        s2=input().strip()
        if first !="":
            if s1==last:
                print(first)
            else:
                print(last)
        else:
            print(out)
        sys.stdout.flush()
        if s1==s2:# and reached==false:
            reached=true
            out=s1
            last=out
            first=s1
        else:
            out=s2
        i+=1
    
    