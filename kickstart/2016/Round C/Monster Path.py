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


def get_pm(r, c, p, q):
    mat = []
    for _ in range(r):
        arr = get_input_array()
        #        arr=[1 if x=="A" else -1 for x in arr]
        mat.append(arr)
    return mat


mp = {}


def get_mats(mat):
    mat_s = []
    for r in mat:
        mat_s.append(" ".join(r))
    return " ".join(mat_s)


def trav_optim(r, c, rs, cs, s, mat, p, q):
    mat_s = get_mats(mat)
    if (rs, cs, mat_s, s) in mp:
        return
    if s == 0:
        mp[(rs, cs, mat_s, s)] = 0
        return
    d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    ans = []
    for dd in d:
        r_s = rs + dd[0]
        c_s = cs + dd[1]
        if r_s >= 0 and r_s < r and c_s >= 0 and c_s < c:
            prob = 0
            if mat[r_s][c_s][0] == 'A':
                prob = pow(1 - p, len(mat[r_s][c_s]) - 1) * p
                mat[r_s][c_s] += 'A'
                trav_optim(r, c, r_s, c_s, s - 1, mat, p, q)
                mat_s_ = get_mats(mat)
                ans.append(prob + mp[(r_s, c_s, mat_s_, s - 1)])
                mat[r_s][c_s] = mat[r_s][c_s][:-1]
            else:
                prob = pow(1 - q, len(mat[r_s][c_s]) - 1) * q
                mat[r_s][c_s] += '.'
                trav_optim(r, c, r_s, c_s, s - 1, mat, p, q)
                mat_s_ = get_mats(mat)
                ans.append(prob + mp[(r_s, c_s, mat_s_, s - 1)])
                mat[r_s][c_s] = mat[r_s][c_s][:-1]
    ans.append(0)  # if its 1x1 grid
    mp[(rs, cs, mat_s, s)] = max(ans)


for tt in range(1, 1 + t):
    r, c, rs, cs, s = get_int_input_array()
    p, q = get_float_input_array()
    mat = get_pm(r, c, p, q)
    mp = {}
    trav_optim(r, c, rs, cs, s, mat, p, q)
    ans = mp[(rs, cs, get_mats(mat), s)]
    print("Case #" + str(tt) + ": " + str(ans))