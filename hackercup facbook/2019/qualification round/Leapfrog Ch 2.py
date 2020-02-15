f=open("leapfrog_ch_.txt")
line=f.readline()
t= int(line.strip())
ff=open("output.out","w+")
for i in range(1,t+1):
    arr=f.readline().strip()
    dot=0
    B=0
    n=len(arr)
    j=0
    while j<n:
        if arr[j] =="A":
            break
        j+=1
    j+=1
    while j<n:
        if arr[j]=="B":
            B+=1
        elif arr[j]==".":
            dot+=1
        j+=1
    ans="Y"
    
    if dot>B:
        if B<2:
            ans="N"
    elif dot==0 and n!=1:
        ans="N"
    ff.write("Case #"+str(i)+": "+ans+"\n")
ff.close()
f.close()