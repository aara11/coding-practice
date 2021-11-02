from collections import defaultdict


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
    w, n = get_int_input_array()
    x = get_int_input_array()
    #    x=[p-1 for p in x]
    freq = defaultdict(lambda: 0)
    for xx in x:
        freq[xx] += 1
    freq_k = []
    for k, v in freq.items():
        freq_k.append([k, v])

    freq_k = sorted(freq_k)

    m = len(freq_k)
    for i in range(m):
        freq_k += [[freq_k[i][0] + n, freq_k[i][1]]]
    for i in range(m):
        freq_k += [[freq_k[i][0] + (2 * n), freq_k[i][1]]];

    diff = int(n // 2)
    curr_idx = m - 1
    i = m - 2
    while i >= 0:
        if freq_k[curr_idx][0] - freq_k[i][0] <= diff:
            i -= 1
        else:
            break
    # i is now the index of end :)
    start_idx = i + 1
    end_idx = i + m
    b_s = 0
    b_c = 0
    f_s = 0
    f_c = 0
    for i in range(start_idx, curr_idx):
        b_c += freq_k[i][1]
        b_s += (freq_k[curr_idx][0] - freq_k[i][0]) * freq_k[i][1]

    for i in range(curr_idx + 1, end_idx + 1):
        f_c += freq_k[i][1]
        f_s += (freq_k[i][0] - freq_k[curr_idx][0]) * freq_k[i][1]
    ans = b_s + f_s
    for idx in range(curr_idx + 1, curr_idx + m):
        if end_idx >= idx:
            f_s -= (freq_k[idx][0] - freq_k[idx - 1][0]) * f_c
            f_c -= freq_k[idx][1]
        else:
            end_idx = idx
        b_c += freq_k[idx - 1][1]
        b_s += (freq_k[idx][0] - freq_k[idx - 1][0]) * b_c
        while start_idx < idx:
            if freq_k[idx][0] - freq_k[start_idx][0] > diff:
                b_c -= freq_k[start_idx][1]
                b_s -= (freq_k[idx][0] - freq_k[start_idx][0]) * freq_k[start_idx][1]
                start_idx += 1
            else:
                break

        for e_idx in range(end_idx + 1, start_idx + m):
            f_c += freq_k[e_idx][1]
            f_s += (freq_k[e_idx][0] - freq_k[idx][0]) * freq_k[e_idx][1]

        end_idx = start_idx + m - 1

        ans = min(ans, b_s + f_s)
    print("Case #" + str(tt) + ": " + str(ans))