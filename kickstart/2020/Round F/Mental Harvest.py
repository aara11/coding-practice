from collections import OrderedDict

t = int(input())
for tt in range(1, t + 1):
    n, q = [int(x) for x in input().strip().split()]
    intervals = []
    for i in range(n):
        s, e = [int(x) for x in input().strip().split()]
        intervals.append([s, e])
    ct = 0
    intervals = sorted(intervals, key=lambda ii: ii[0])
    end = 0
    for i in intervals:
        if end <= i[0]:
            end = i[0] + q
            ct += 1
        if end < i[1]:
            inc = (i[1] - end + q - 1) // q
            ct += inc
            end += (inc * q)

    ans = str(ct)
    print("Case #" + str(tt) + ": " + ans)

