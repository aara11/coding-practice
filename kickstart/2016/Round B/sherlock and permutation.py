from collections import defaultdict
def get_input():
    return input().strip()

def get_int_input():
    return int(get_input())

def get_input_array():
    return get_input().split()

def get_int_input_array():
    arr=get_input_array()
    return [int(x) for x in arr]

fact={}
mp={}

def calc(n):
    if n in mp:
        return
    if n==1:
        mp_={}
        mp_[1]=1
        mp[n]=mp_
        fact[1]=1
        return
    calc(n-1)
    fact[n]=fact[n-1]*n
    mp_=defaultdict(lambda : 0)
    ct=0
    for i in range(1,n):
        init_num_comb=mp[i][1]
        rest=mp[n-i]
        for k,v in rest.items():
            mp_[k+1]+=(v*init_num_comb)
            ct+=(v*init_num_comb)
    mp_[1]=fact[n]-ct
    mp[n]=mp_

def get_ans(n,m):
    ans=0
    for k,v in mp[n].items():
        ans+=(k*k*v)
        ans=ans%m
    return ans

t=get_int_input()
for tt in range(1,t+1):
    n,m=get_int_input_array()
    calc(n)
    ans=get_ans(n,m)
    print("Case #"+str(tt)+": "+str(ans))