# 숨바꼭질 4
from collections import deque

# 최종 위치 K에서 부모노드를 따라 N까지 result에 저장
def sol(n):
    while cnt[n] != -2:
        result.append(n)
        n = cnt[n]
    result.append(n)


# 평범한 bfs
def bfs(s):
    q = deque([N])
    while q:
        n = q.popleft()
        # vst[K]깂이 있다면 더이상 진행 x
        if n == K:
            sol(K)
            return
        dn = [1, -1, n]
        x = vst[n]
        # 현재 위치에서 수빈이 이동가능 위치 3군데 확인
        for d in range(3):
            num = n + dn[d]
            # 아직 방문하지 않은 곳이면 vst에 이동횟수 기록
            # cnt[이동위치]에 현재위치 기록
            if 0 <= num <= 100000 and vst[num] == -1:
                vst[num] = x+1
                cnt[num] = n
                q.append(num)
                

N, K = map(int, input().split())

# 방문배열 vst, 부모노드 기록 cnt
vst = [-1] * 100001
cnt = [-1] * 100001
vst[N] = 0
cnt[N] = -2

result = []
bfs(N)

print(vst[K])
print(*result[::-1])