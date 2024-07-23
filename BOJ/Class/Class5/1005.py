# ACM Craft / 골드3

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    cost = list(map(int, input().split()))
    s = [[] for _ in range(N+1)]
    p = [[] for _ in range(N+1)]
    for _ in range(K):
        X, Y = map(int, input().split())
        s[X].append(Y)
        p[Y].append(X)
    W = int(input())

    S = 0
    for e in range(1, N+1):
        if not p[e]:
            S = e
    
    arr = [[S]]
    vst = [0] * (N+1)
    vst[S] = 1
    cnt = 1
    idx = 0
    while True:
        tmp = []
        for i in arr[idx]:
            for x in s[i]:
                if vst[x] == 0:
                    flag = True
                    for y in p[x]:
                        if vst[y] == 0:
                            flag = False
                    if flag:
                        vst[x] = 1
                        tmp.append(x)
        if tmp:
            arr.append(tmp)
            idx += 1
        else:
            break
    
    road = [W]
    vst = [0] * (N+1)
    vst[W] = 1
    q = [W]
    while q:
        x = q.pop(0)
        if x == S:
            break
        for y in p[x]:
            if vst[y] == 0:
                q.append(y)
                road.append(y)

    result = 0
    for lst in arr:
        if W in lst:
            break
        result += max(cost[x-1] if x in road else 0 for x in lst)
    result += cost[W-1]
    print(result)