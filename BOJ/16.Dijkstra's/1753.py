# 최단경로
# 그래프이론, 다익스트라

import sys
input = sys.stdin.readline
import heapq

def sol(s):
    # 시작지점은 0
    dist[s] = 0
    # 가중치의 합을 우선순위로 하는 queue
    q = []
    heapq.heappush(q, (dist[s], s))
    while q:
        v, s = heapq.heappop(q)
        # v보다 dist[s]가 작은 값이라면 이미 다른 경로에서 최소처리한 경우이므로 제외
        # 뒤늦게 큐에서 나온 값을 계산하는 것은 불필요
        if dist[s] < v:
            continue
        # 최소라면 해당 정점에서 이어진 정점의 경로 값 갱신
        for e, w in arr[s]:
            # 다른 경로를 통해 저장된 값 or 초기화 된 값 보다 작다면 최소경로로 저장
            if v + w < dist[e]:
                dist[e] = min(dist[e], v + w)
                heapq.heappush(q, (dist[e], e))


V, E = map(int, input().split())
K = int(input())

arr = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int,input().split())
    arr[a].append((b,c))

dist = [10*V] * (V+1)
sol(K)

for i in range(1, V+1):
    if dist[i] == 10*V:
        dist[i] = 'INF'
    print(dist[i])
