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
    mp = {}
    n = get_int_input()
    arr = get_int_input_array()
    ans = 0;
    while n > 1:
        n -= 1
        for i in range(n):
            ans += (arr[i] + arr[i + 1]) / n
            agg = arr[i] * (n - i - 1)
            agg += arr[i] + arr[i + 1]
            agg += arr[i + 1] * i
            arr[i] = agg / n

    print("Case #" + str(tt) + ": " + str(ans))