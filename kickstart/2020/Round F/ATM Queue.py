from collections import OrderedDict

t = int(input())
for tt in range(1, t + 1):
    n, q = [int(x) for x in input().strip().split()]
    arr = [int(x) for x in input().strip().split()]

    od = {}
    for i in range(n):
        a = arr[i]
        key = (a + q - 1) // q
        if key not in od:
            od[key] = []
        od[key].append(i)
    od = OrderedDict(sorted(od.items(), key=lambda t: t[0]))
    ans = ""
    for k, v in od.items():
        for vv in v:
            ans += " " + str(vv + 1)
    print("Case #" + str(tt) + ": " + ans)

