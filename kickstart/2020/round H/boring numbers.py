def input_():
    return input()


def get_input():
    return input_().strip()


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

dic = {}
dic[0] = 1


def get_all(i):
    if i in dic:
        return dic[i]
    dic[i] = dic[i - 1] * 5
    return dic[i]


def check(digit, i):
    # 0th position-> odd, 1st position -> even
    return (digit + i) % 2 == 1


def get_all_comb(val):
    val_ = str(val)
    n = len(val_)
    ans = 0
    for i in range(1, n):
        ans += get_all(i)
    for i in range(n):
        if i == 0 or check(int(val_[i - 1]), i - 1):
            a = int(val_[i])
            if i % 2 == 0:
                num = int(a // 2)
            else:
                num = int((a + 1) // 2)
            ans += num * dic[n - 1 - i]
            if i == n - 1 and i % 2 == 0 and a % 2 == 1:
                ans += 1
            elif i == n - 1 and i % 2 == 1 and a % 2 == 0:
                ans += 1
        else:
            break
    return ans


for tt in range(1, 1 + t):
    l, r = get_int_input_array()
    ans = get_all_comb(r) - get_all_comb(l - 1)
    print("Case #" + str(tt) + ": " + str(ans))