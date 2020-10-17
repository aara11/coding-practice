from collections import defaultdict

mp = {}


def get_poss(curr_state, target, m, k):
    possibilities = 0
    lst = []
    d = defaultdict(lambda: [])
    used = 0
    for i in range(k - 1, -1, -1):
        if curr_state[i] < target[i] or curr_state[i] in d.keys():
            d[curr_state[i]].append(i)
            if curr_state[i] == 0:
                possibilities = m
            if possibilities != m:
                possibilities += 1
        else:
            used += 1
    if possibilities == m:
        possibilities -= used

    return possibilities, d


def calc(curr_state, target, m, k):
    curr_state = sorted(curr_state)
    if tuple(curr_state) in mp:
        return
    poss, curr_idx = get_poss(curr_state, target, m, k)
    if poss == 0:
        mp[(tuple(curr_state))] = 0
        return
    expected = m / poss
    ct_zero = poss
    for key, v in curr_idx.items():
        if key != 0:
            ct_zero -= len(v)
        curr_s = curr_state.copy()
        curr_s[v[0]] += 1
        calc(curr_s, target, m, k)
    for key, v in curr_idx.items():
        curr_s = curr_state.copy()
        curr_s[v[0]] += 1
        curr_s = sorted(curr_s)
        if key == 0:
            expected += (ct_zero * mp[tuple(curr_s)] / poss)
        else:
            expected += (len(v) * mp[tuple(curr_s)] / poss)
    mp[(tuple(curr_state))] = expected


t = int(input())
for tt in range(1, t + 1):
    n, m, k = [int(x) for x in input().strip().split()]
    target = []
    for _ in range(k):
        target.append(int(input()))
    target = tuple(sorted(target))
    curr_state = [0 for _ in range(k)]
    calc(curr_state, target, m, k)
    ans = mp[tuple(curr_state)]
    print("Case #" + str(tt) + ": " + str(ans))
    mp = {}