# 효율적인 해킹
# pypy3 통과

from collections import deque

def sol(n):
    global max_count, result

    tmp = [0] * (N+1)
    tmp[n] = 1

    queue = deque([n])
    while queue:
        s = queue.popleft()
        for e in arr[s]:
            if tmp[e] == 0:
                tmp[e] = 1
                queue.append(e)

    N_count = sum(tmp)    
    if max_count == N_count:
        result.append(n)
    elif max_count < N_count:
        max_count = N_count
        result = [n]
    return


N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[b].append(a)

max_count = 0
result = []

for i in range(1, N+1):
    sol(i)

print(' '.join(str(i) for i in result))
