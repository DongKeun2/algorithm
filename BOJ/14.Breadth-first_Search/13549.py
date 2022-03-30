# 숨바꼭질 3

from collections import deque

# bfs
def bfs(s):
    q = deque([N])
    while q:
        n = q.popleft()
        if n == K:
            return
        dn = [n, 1, -1]
        x = vst[n]
        for d in range(3):
            num = n + dn[d]
            if 0 <= num <= 100000 and vst[num] == -1:
                if d == 0:
                    vst[num] = x
                    q.appendleft(num)
                else:
                    vst[num] = x+1
                    q.append(num)
                

N, K = map(int, input().split())

vst = [-1] * 100001
vst[N] = 0

bfs(N)

print(vst[K])
