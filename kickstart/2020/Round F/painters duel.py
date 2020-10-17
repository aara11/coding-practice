mp = {}


def get_point(r, p):
    return ((r - 1) * (r - 1)) + p


def get_neighbor(r, p, filled, s):
    lst = []
    if p % 2 == 1:
        if p > 1:
            left = get_point(r, p - 1)
            lst.append([left, r, p - 1])
        if p < 2 * r - 1:
            right = get_point(r, p + 1)
            lst.append([right, r, p + 1])
        if r < s:
            down = get_point(r + 1, p + 1)
            lst.append([down, r + 1, p + 1])
    else:
        left = get_point(r, p - 1)
        lst.append([left, r, p - 1])
        right = get_point(r, p + 1)
        lst.append([right, r, p + 1])
        if r > 1:
            up = get_point(r - 1, p - 1)
            lst.append([up, r - 1, p - 1])
    neigh = []
    for l in lst:
        if l[0] not in filled:
            neigh.append(l)
    return neigh


def get_opt(s, ra, pa, rb, pb, filled, filled_lst):
    if (ra, pa, rb, pb, s, tuple(filled_lst)) in mp:
        return
    na = get_neighbor(ra, pa, filled, s)
    if len(na) == 0:
        nb = get_neighbor(rb, pb, filled, s)
        if len(nb) == 0:
            mp[(ra, pa, rb, pb, s, tuple(filled_lst))] = 0
        else:
            get_opt(s, rb, pb, ra, pa, filled, filled_lst)
            mp[(ra, pa, rb, pb, s, tuple(filled_lst))] = -1 * mp[(rb, pb, ra, pa, s, tuple(filled_lst))]
    else:
        ans = []
        fill = filled.copy()
        for n in na:
            fill[n[0]] = None
            filled_lst_ = sorted(fill.keys())
            get_opt(s, rb, pb, n[1], n[2], fill, filled_lst_)
            del fill[n[0]]
            ans.append(1 - mp[(rb, pb, n[1], n[2], s, tuple(filled_lst_))])
        mp[(ra, pa, rb, pb, s, tuple(filled_lst))] = max(ans)


t = int(input())
for tt in range(1, t + 1):
    s, ra, pa, rb, pb, c = [int(x) for x in input().strip().split()]
    filled = {}
    for i in range(c):
        r, p = [int(x) for x in input().strip().split()]
        filled[get_point(r, p)] = None
    filled[get_point(ra, pa)] = None
    filled[get_point(rb, pb)] = None
    filled_lst = sorted(filled.keys())
    get_opt(s, ra, pa, rb, pb, filled, filled_lst)
    ans = mp[(ra, pa, rb, pb, s, tuple(filled_lst))]
    print("Case #" + str(tt) + ": " + str(ans))