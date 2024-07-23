# 숨바꼭질 2 / 골드4

from collections import deque

N, K = map(int, input().split())
lst = [0] * 100001

q = deque([N])
answer = 0
cnt = 0
while q:
    s = q.popleft()
    if s == K:
        answer = lst[s]
        cnt += 1
    else:
        for e in (s+1, s-1, s*2):
            if 0 <= e <= 100000 and (lst[e] == 0 or lst[e] == lst[s]+1):
                lst[e] = lst[s] + 1
                q.append(e)
print(answer)
print(cnt)