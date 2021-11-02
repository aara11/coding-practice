def get_input():
    return input().strip()


def get_int_input():
    return int(get_input())


def get_input_array():
    return get_input().split()


def get_int_input_array():
    arr = get_input_array()
    return [int(x) for x in arr]


def get_float_input_array():
    arr = get_input_array()
    return [float(x) for x in arr]


t = get_int_input()

for tt in range(1, 1 + t):
    s = get_input()
    n = len(s)
    ks = []
    for i in range(n):
        if s[i] == "K":
            if s[i:i + 4] == "KICK":
                ks.append("K")
        elif s[i] == "S":
            if s[i:i + 5] == "START":
                ks.append("S")
    m = len(ks)
    ans = 0
    ct = 0
    for i in range(m - 1, -1, -1):
        if ks[i] == "S":
            ct += 1
        else:
            ans += ct

    print("Case #" + str(tt) + ": " + str(ans))
