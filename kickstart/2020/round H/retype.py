def input_():
    return input()
def get_input():
    return input_().strip()

def get_int_input():
    return int(get_input())

def get_input_array():
    return get_input().split()

def get_int_input_array():
    arr=get_input_array()
    return [int(x) for x in arr]

def get_float_input_array():
    arr=get_input_array()
    return [float(x) for x in arr]

t=get_int_input()

for tt in range(1,1+t):
    n,k,s = get_int_input_array()
    ans=k-1
    r1=max(n+1,0)#restart
    r2=max(k-s,0) + max(n-s+1,0)
    ans=ans+min(r1,r2)
    print("Case #"+str(tt)+": "+str(ans))