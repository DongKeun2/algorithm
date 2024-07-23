# 아기 상어 / 골드3

from heapq import heappush, heappop

di, dj = (-1, 0, 1, 0), (0, -1, 0, 1)
def find_feed(ni, nj):
    q = []
    heappush(q, (0, ni, nj))
    vst = [[0]*N for _ in range(N)]
    vst[ni][nj] = 1
    tmp = [10**16, 0, 0]
    while q:
        dist, si, sj = heappop(q)
        for d in range(4):
            ei, ej = si + di[d], sj + dj[d]
            if 0 <= ei < N and 0 <= ej < N and vst[ei][ej] == 0 and arr[ei][ej] <= size:
                if arr[ei][ej] and arr[ei][ej] < size:
                    if dist + 1 > tmp[0]:
                        return tmp
                    elif dist + 1 < tmp[0]:
                        tmp = [dist + 1, ei, ej]
                    else:
                        if ei < tmp[1]:
                            tmp = [dist + 1, ei, ej]
                        else:
                            if ei == tmp[1] and ej < tmp[2]:
                                tmp = [dist + 1, ei, ej]
                vst[ei][ej] = 1
                heappush(q, (dist+1, ei, ej))
    if tmp[0] == 10**16: return [0, 0, 0]
    return tmp


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ni, nj = 0, 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            arr[i][j] = 0
            ni, nj =i, j
size = 2
cnt = 0
answer = 0
while True:
    dist, ei, ej = find_feed(ni,  nj)
    if dist:
        arr[ei][ej] = 0
        ni, nj = ei, ej
        answer += dist
        cnt += 1
        if cnt >= size:
            size += 1
            cnt = 0
    else:
        break
print(answer)