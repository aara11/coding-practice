ERR = .000001
t = int(input())
for tt in range(1, t + 1):
    m = int(input())
    c = [int(x) for x in input().strip().split()]
    beg = -1
    end = 1
    while end - beg > ERR:
        mid = (beg + end) / 2
        ans = 0
        fac = 1
        rate = 1 + mid
        for i in range(m, 0, -1):
            ans += (fac * c[i])
            fac = fac * rate
        ans -= (fac * c[0])
        if ans == 0:
            break
        if ans > 0:
            beg = mid
        else:
            end = mid
    ans = (beg + end) / 2
    print("Case #" + str(tt) + ": " + str(ans))


