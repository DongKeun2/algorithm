# 소 운전한다.
# 다익스트라
# ing

import sys
input = sys.stdin.readline
import heapq

def sol(s):
    pass

V, E = map(int, input().split())

arr = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, t, k = map(int,input().split())
    arr[s].append((t, k, e))
    arr[e].append((t, k, s))

dist = [20000*V] * (V+1)
result = [20000*V] * (V+1)
sol(1)

for i in range(2, len(result)):
    print(result[i])
