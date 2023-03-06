# [인증평가(1차) 기출] 로봇이 지나간 경로 Lv3
# 105ms 37.71Mb

import sys
from collections import deque
input = sys.stdin.readline

# 하 우 상 좌
dl = ['v', '>', '^', '<']
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
def sol(si, sj, sd):
    global answer

    q = deque([(si, sj, sd)])
    while q:
        # 기존 위치와 방향
        i, j, sd = q.popleft()
        for d in range(4):
            ei = i + di[d]
            ej = j + dj[d]
            # 방향 전환 여부 확인
            if 0 <= ei < H and 0 <= ej < W and arr[ei][ej] == '#' and vst[ei][ej] == 0:
                if (d - sd) % 4 == 1:
                    answer += 'L'
                elif (sd - d ) % 4 == 1:
                    answer += 'R'

                # 방향 전환 후 2칸 전진
                answer += 'A'
                for c in range(1, 3):
                    ei = i + c * di[d]
                    ej = j + c * dj[d]
                    vst[ei][ej] = 1
                    if c == 2:
                        q.append((ei, ej, d))
                break


H, W = map(int, input().split())
arr = [list(input().strip()) for _ in range(H)]

# 시작 지점 여부 판단
# 4방향 중 한 방향만 갈 수 있는 곳
si, sj = 0, 0
answer = ''
vst = [[0]*W for _ in range(H)]
for i in range(H):
    if si:
        break
    for j in range(W):
        if arr[i][j] == '#':
            cnt = 0
            sd = -1
            for d in range(4):
                ei = i + di[d]
                ej = j + dj[d]
                if 0 <= ei < H and 0 <= ej < W and arr[ei][ej] == '#':
                    cnt += 1
                    sd = d
            if cnt == 1:
                sol(i, j, sd)
                si = i+1
                sj = j+1
                break

print(si, sj)
print(dl[sd])
print(answer)