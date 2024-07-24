# 연결 요소의 개수

from collections import deque
import sys
input = sys.stdin.readline

def sol(n):
    q = deque()
    q.append(n)
    while q:
        s = q.popleft()
        for m in arr[s]:
            if vst[m] == 0:
                vst[m] = 1
                q.append(m)
    return


N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

vst = [0] * (N+1)
vst[0] = 1

cnt = 0
for i in range(1, N+1):
    if vst[i] == 0:
        vst[i] = 1 
        cnt += 1
        sol(i)

print(cnt)