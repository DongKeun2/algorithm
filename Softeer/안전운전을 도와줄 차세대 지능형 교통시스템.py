# [인증평가(1차) 기출] 안전운전을 도와줄 차세대 지능형 교통시스템 Lv3
# 308ms 50.33Mb

import sys

# 하 우 상 좌
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
# direct, 방향
signal = [
    [],
    [0, 1, 2],
    [1, 2, 3],
    [0, 2, 3],
    [0, 1, 3],
    [1, 2],
    [2, 3],
    [0, 3],
    [0, 1],
    [0, 1],
    [1, 2],
    [2, 3],
    [0, 3],
]
def sol(si, sj, d, t):
    global answer
    if t >= T:
        return

    s = arr[si][sj][t%4]
    if d == s%4:
        for x in signal[s]:
            ei = si + di[x]
            ej = sj + dj[x]
            if 0 <= ei < N and 0 <= ej < N:
                if vst[ei][ej] == 0:
                    answer += 1
                vst[ei][ej] = 1
                sol(ei, ej, x, t+1)
            

N, T = map(int, input().split())
arr = [[] for _ in range(N)]
for i in range(N*N):
    arr[i//N].append(list(map(int, input().split())))

vst = [[0]*N for _ in range(N)]
vst[0][0] = 1
answer = 1
sol(0, 0, 2, 0)
print(answer)