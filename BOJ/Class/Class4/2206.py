# 벽 부수고 이동하기 / 골드3

from heapq import heappop, heappush

N, M = map(int, input().split())
arr = [input() for _ in range(N)]

di, dj = (0, 1, 0, -1), (1, 0, -1, 0)
def sol():
    q = []
    heappush(q, (0, 1, 0, 0))
    while q:
        flag, cnt, si, sj = heappop(q)
        for d in range(4):
            ei, ej = si + di[d], sj + dj[d]
            if 0 <= ei < N and 0 <= ej < M and vst[ei][ej] > cnt + 1:
                if arr[ei][ej] == '0':
                    if ei == N-1 and ej == M-1:
                        vst[ei][ej] = cnt + 1
                    else:
                        heappush(q, (flag, cnt+1, ei, ej))
                        vst[ei][ej] = cnt + 1
                else:
                    if not flag:
                        heappush(q, (1, cnt+1, ei, ej))
                        vst[ei][ej] = cnt + 1
    if vst[N-1][M-1] == N*M:    return -1
    return vst[N-1][M-1]
vst = [[N*M] * M for _ in range(N)]
vst[0][0] = 1
print(1 if N == 1 and M == 1 else sol())