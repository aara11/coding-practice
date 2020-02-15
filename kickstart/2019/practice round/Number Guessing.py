import sys 
t=int(input().strip())

for _ in range(t):
    a,b=[int(x) for x in input().strip().split()]
    n=input()
    while True:
        m=(a+b+1)//2
        print(m)
        sys.stdout.flush()
        s=input().strip()
        if s=="CORRECT":
            break;
        if s=="TOO_SMALL":
            a=m
        else:
            b=m-1
            