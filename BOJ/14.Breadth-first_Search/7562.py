# 나이트의 이동
# 그래프이론, 그래프탐색, 너비우선탐색

from collections import deque

def sol(si, sj, ei, ej):
    q = deque()
    q.append([si, sj])
    while q:
        ni, nj = q.popleft()
        if ni == ei and nj == ej:
            return
        n = arr[ni][nj]
        for d in range(8):
            ii = ni + di[d]
            jj = nj + dj[d]
            if 0 <= ii < I and 0 <= jj < I and arr[ii][jj] == 0:
                arr[ii][jj] = n+1
                q.append([ii, jj])
    return

# 나이트가 이동 가능한 8방향
di = [2, 1, -1, -2, -2, -1, 1, 2]
dj = [1, 2, 2, 1, -1, -2, -2, -1]

T = int(input())
for test_case in range(T):
    I = int(input())
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())

    # 나이트가 해당 위치에 가기 위해 이동한 횟수를 저장하는 배열
    arr =[[0 for _ in range(I)] for _ in range(I)]
    sol(si, sj, ei, ej)

    # 최종 위치까지 이동한 횟수 출력
    print(arr[ei][ej])
    