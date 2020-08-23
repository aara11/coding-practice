t=int(input())

for tt in range(1,t+1):
    s=input()
    print("Case #"+str(tt)+":")
    n=len(s)
    print("+-" + "-"*n + "-+")
    print("| "+s+" |")
    print("+-" + "-"*n + "-+")