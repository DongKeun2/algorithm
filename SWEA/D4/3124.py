# 최소 스패닝 트리

def find_set(n):
    tmp = []
    while n != rep[n]:
        tmp.append(n)
        n = rep[n]
    for m in tmp:
        rep[m] = n
    return n
 
 
def union(u, v):
    rep[find_set(v)] = find_set(u)
 
 
T = int(input())
 
for test_case in range(1, T+1):
    V, E = map(int, input().split())
 
    arr = []
    for _ in range(E):
        u, v, w = map(int, input().split())
        arr.append((w, u, v))
    arr.sort()
 
    rep = [i for i in range(V+1)]
 
    result = 0
    cnt = 0
    for w, u, v in arr:
        if cnt >= V-1:
            break
        if find_set(u) != find_set(v):
            cnt += 1
            result += w
            union(u, v)
 
    print(f'#{test_case} {result}')