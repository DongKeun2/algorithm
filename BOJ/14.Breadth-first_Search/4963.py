# 섬의 개수

from collections import deque
import sys
input = sys.stdin.readline

def sol(si, sj):
    q = deque()
    q.append([si, sj])
    while q:
        si, sj = q.popleft()
        for d in range(8):
            ni, nj = si+di[d], sj+dj[d]
            if 0<=ni<b and 0<=nj<a and arr[ni][nj] == 1:
                arr[ni][nj] = 0
                q.append([ni, nj])


di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(b)]
    cnt = 0
    for i in range(b):
        for j in range(a):
            if arr[i][j] == 1:
                arr[i][j] = 0
                sol(i, j)
                cnt += 1
    print(cnt)