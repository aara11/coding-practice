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
    n = get_int_input()
    mat = []
    for i in range(n):
        mat.append(get_int_input_array())
    ans = 0
    for i in range(n):
        s = 0
        for j in range(n - i):
            s += mat[i + j][j]
        ans = max(ans, s)
    for j in range(1, n):
        s = 0
        for i in range(n - j):
            s += mat[i][i + j]
        ans = max(ans, s)

    print("Case #" + str(tt) + ": " + str(ans))