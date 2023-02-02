# 장애물 인식 프로그램 Lv2

import sys
input = sys.stdin.readline

# BFS로 장애물 수 확인
def sol(i, j):
    q = [(i, j)]
    cnt = 1
    while q:
        si, sj = q.pop(0)
        for d in range(4):
            ei = si + di[d]
            ej = sj + dj[d]
            if 0 <= ei < n and 0 <= ej < n and arr[ei][ej] and not vst[ei][ej]:
                q.append((ei, ej))
                vst[ei][ej] = 1
                cnt += 1
    return cnt


n = int(input())
arr = [list(map(int, input().strip())) for _ in range(n)]

lst = []
di = [0, 1, 0, -1]
dj = [1, 0, -1 ,0]
vst = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] and not vst[i][j]:
            vst[i][j] = 1
            lst.append(sol(i, j))

# 오름차순 정렬
lst.sort()
print(len(lst))
for result in lst:
    print(result)