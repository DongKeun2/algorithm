# DFS와 BFS

from collections import deque

def dfs(vst1, s):
    st = [s]
    result1.append(s)
    vst1[s] = 1
    for x in arr[s]:
        if vst1[x] == 0:
            dfs(vst1, x)
    return


def bfs(vst2, V):
    q = deque()
    result2.append(V)
    vst2[V] = 1
    q.append(V)
    while q:
        s = q.popleft()
        for x in arr[s]:
            if vst2[x] == 0:
                vst2[x] = 1
                result2.append(x)
                q.append(x)
    return


N, M, V = map(int, input().split())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
for i in range(N+1):
    arr[i].sort()

vst1 = [0] * (N+1)
result1 = []
dfs(vst1, V)

vst2 = [0] * (N+1)
result2 = []
bfs(vst2, V)

print(*result1)
print(*result2)