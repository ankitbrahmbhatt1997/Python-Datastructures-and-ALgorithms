def possible(z):
    for i in dis:
        if i in lands:
            z -= lands[i]
        if i in towns:
            if z >= towns[i][0]:
                z += towns[i][1]
    return z > 0


T = int(input())

while T > 0:
    x = int(input())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    nb = b[0]
    nc = c[0]
    lands = {}
    towns = {}
    p = []
    q = []
    dis = []
    for i in range(1, len(b), 2):
        lands[b[i]] = b[i+1]
        p.append(b[i])
    for i in range(1, len(c), 3):
        towns[c[i]] = (c[i+1], c[i+2])
        q.append(c[i])
    i = 0
    j = 0
    while i < nb and j < nc:
        if p[i] < q[j]:
            dis.append(p[i])
            i += 1
        else:
            dis.append(q[j])
            j += 1
    if i < nb:
        dis.extend(p[i:])
    if j < nc:
        dis.extend(q[j:])
    m = 1
    for y in range(2, len(b), 2):
        m += b[y]
    print(m)
    lo = 1
    hi = m
    res = m
    while(lo <= hi):
        mid = (lo+hi)//2
        if(possible(mid)):
            res = min(mid, res)
            hi = mid - 1
        else:
            lo = mid + 1
    print(res)
    T -= 1
