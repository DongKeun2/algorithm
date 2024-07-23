# 치킨 배달 / 골드5

from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

home = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home.append((i, j))
home_cnt = len(home)

dist = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            tmp = []
            for ei, ej in home:
                tmp.append(abs(i - ei) + abs(j - ej))
            dist.append(tmp)

answer = 10 ** 16
for lst in list(combinations(range(len(dist)), M)):
    home = [[0] * M for _ in range(home_cnt)]
    for i in range(home_cnt):
        for j in range(M):
            home[i][j] = dist[lst[j]][i]
    cnt = 0
    for h in home:
        cnt += min(h)
    if answer > cnt:
        answer = cnt
print(answer)