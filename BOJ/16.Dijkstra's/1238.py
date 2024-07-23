# 파티 # 골드3
# 다익스트라, 그래프, 최단 경로

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())

arr1 = [[] for _ in range(N)]
arr2 =  [[] for _ in range(N)]
for _ in range(M):
    S, E, T = map(int, input().split())
    arr1[S-1].append((E-1,T))
    arr2[E-1].append((S-1, T))

def sol(arr):
    q = []
    heappush(q, (0, X-1))
    lst = [10**16] * N
    lst[X-1] = 0
    while q:
        tot, s = heappop(q)
        for e, t in arr[s]:
            if lst[e] > tot+t:
                lst[e] = tot+t
                heappush(q, (tot+t, e))

    for i in range(N):
        answer[i] += lst[i]

answer = [0] * N
sol(arr1)
sol(arr2)
print(max(answer))
