# 숨바꼭질 3 / 골드5

from heapq import heappush, heappop

N, K = map(int, input().split())
lst = [10**16] * 100001
lst[N] = 0

q = []
heappush(q, (0, N))
while q:
    t, s = heappop(q)
    if 0 <= s+1 <= 100000 and lst[s+1] > t+1:
        lst[s+1] = t+1
        heappush(q, (t+1, s+1))
    if 0 <= s-1 <= 100000 and lst[s-1] > t+1:
        lst[s-1] = t+1
        heappush(q, (t+1, s-1))
    if 0 <= s*2 <= 100000 and lst[s*2] > t:
        lst[s*2] = t
        heappush(q, (t, s*2))
print(lst[K])