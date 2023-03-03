# 동계 테스트 시점 예측 Lv3

import sys
from collections import deque
input = sys.stdin.readline

# arr, BFS활용 0 => -1
# tmp, arr에서 -1이 아닌 곳에서 -1과 맞닿아 있는 개수
# arr 재배치, -1과 vst에서 2이상을 0으로 초기화

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
def bfs():
    q = deque([(0,0)])
    vst = [[0]*M for _ in range(N)]
    vst[0][0] = 1
    cnt = 1
    while q:
        si, sj = q.popleft()
        for d in range(4):
            ei = si + di[d]
            ej = sj + dj[d]
            if 0 <= ei < N and 0 <= ej < M and arr[ei][ej] == 0 and vst[ei][ej] == 0:
                arr[ei][ej] = -1
                vst[ei][ej] = 1
                cnt += 1
                q.append((ei, ej))
    if cnt >= N*M:
        return False
    return True

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
while True:
    if bfs():
        result += 1
        tmp = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                for d in range(4):
                    ei = i + di[d]
                    ej = j + dj[d]
                    if 0 <= ei < N and 0 <= ej < M and arr[ei][ej] == -1:
                        tmp[i][j] += 1

        for i in range(N):
            for j in range(M):
                if arr[i][j] == -1 or tmp[i][j] >= 2:
                    arr[i][j] = 0
    else:
        break

print(result)