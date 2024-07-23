# 웜홀 / 골드3
# Bellman-Ford

import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    road = [[] for _ in range(N+1)]
    for _ in range(M):
        S, E, T = map(int, input().split())
        road[S].append((E, T))
        road[E].append((S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        road[S].append((E, -T))


    def sol():
        slst = range(1, (N+1))
        check_set = set()
        while slst:
            if slst in check_set:
                return True
            check_set.add(slst)
            
            tmp_lst = []
            for s in slst:
                for e, t in road[s]:
                    if dist[e] > dist[s] + t:
                        dist[e] = dist[s] + t
                        tmp_lst.append(e)
            slst = tuple(tmp_lst)
        return False

    dist = [10**16] * (N+1)
    print('YES' if sol() else 'NO')
    