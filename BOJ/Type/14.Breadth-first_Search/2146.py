# 다리 만들기

from collections import deque

# 육지와 연결된 바다에서 bfs
def sol(si, sj, dd):
    global result

    vst = [[0 for _ in range(N)] for _ in range(N)]
    vst[si][sj] = 1
    q = deque([])
    q.append([si, sj])
    while q:
        si, sj = q.popleft()
        n = vst[si][sj]

        # 이미 만들어진 다리의 최솟값을 넘어서면 종료
        if n >= result:
            return

        # 상, 하 좌, 우 중 육지와 맞닿아 있는 방향은 제외하고 탐색
        for d in range(4):
            if d != (dd+2)%4:
                ni = si + di[d]
                nj = sj + dj[d]
    
                if 0 <= ni < N and 0 <= nj < N and vst[ni][nj] == 0:
                    # 바다라면 다리 설치
                    if arr[ni][nj] == 0:
                        vst[ni][nj] = n+1
                        q.append([ni, nj])

                    # 다른 섬과 만났다면 결과 갱신
                    elif arr[ni][nj] == 1:
                        if result > n:
                            result = n
                        return


# 해당 지점의 섬을 모두 2로 변경 
# => 그 지점들 중 바다와 맞닿아 있는 지점 다리만들기
def check(si, sj):
    arr[si][sj] = 2
    q = deque([])
    q.append([si, sj])
    go = [[si, sj]]
    while q:
        si, sj = q.popleft()
        for d in range(4):
            ei = si + di[d]
            ej = sj + dj[d]
            if 0 <= ei < N and 0 <= ej < N and arr[ei][ej] == 1:
                arr[ei][ej] = 2
                q.append([ei, ej])
                go.append([ei, ej])
    
    # go에 섬의 모든 지점을 저장, 상하좌우탐색 바다라면 sol 호출
    for i, j in go:
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                sol(ni, nj, d)


# 상, 좌, 하 우
# 반대방향을 제외하기 위해 편하게 설정
di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 육지에서 확인
result = N*N
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            check(i, j)

print(result)