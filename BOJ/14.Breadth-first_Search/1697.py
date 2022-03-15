# 숨바꼭질
# 그래프이론, 그래프탐색, 너비우선탐색

from collections import deque

N, K = map(int, input().split())

# 0부터 100000까지 각각 얼마나 걸리는 지 저장할 배열
vst = [-1] * 100001

# N은 0초 후에 도착
vst[N] = 0
q = deque([N])

# bfs
while q:
    n = q.popleft()
    dn = [1, -1, n]
    x = vst[n]

    # K에서 왔다면 종료 (이미 vst[K]에 저장)
    if n == K:
        break

    # ex) N에서 출발하여 N-1, N+2, 2N 에 1 저장 => Q에 추가하고 반복
    for d in range(3):
        num = n + dn[d]
        if 0 <= num <= 100000 and vst[num] == -1:
            vst[num] = x+1
            q.append(num)

print(vst[K])
