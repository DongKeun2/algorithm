# 마인크래프트 / 실버2

N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = [0] * 257
for i in range(N):
    for j in range(M):
        lst[arr[i][j]] += 1

answer = [500*500*256*2, -1]
for h in range(257)[::-1]:
    time = 0
    cnt = B
    for i in range(257):
        cnt += (i - h) * lst[i]
        if i < h:
            time += (h - i) * lst[i]
        elif i > h:
            time += 2 * (i - h) * lst[i]
    if cnt >= 0 and answer[0] > time:
        answer = [time, h]

print(*answer)
                       
