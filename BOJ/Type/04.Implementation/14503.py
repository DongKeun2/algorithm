# 로봇 청소기
# 구현, 시뮬레이션

N, M = map(int, input().split())
si, sj, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 입력받은 d는 시계방향 (북, 동, 남, 서 => 북, 서, 남, 동)
if d%2:
    d = (d+2)%4

# 반시계 방향으로 북, 서, 남, 동
di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

# 시작지점 청소
arr[si][sj] = 2
cnt = 1

flag = 0
while True:
    if flag == -1:
        break
    
    # 현재 방향(d)에서 왼쪽으로 돌며 확인
    for k in range(d+1, d+5):
        c = k%4
        ni = si + di[c]
        nj = sj + dj[c]

        # 청소할 영역이 있으면 청소
        if 1 <= ni < N-1 and 1 <= nj < M-1 and arr[ni][nj] == 0:
            arr[ni][nj] = 2
            si = ni
            sj = nj
            d = c
            cnt += 1
            break
    
    # 4방향 모두 청소할 구역이 없다면 뒤로가거나 종료
    else:
        ni = si - di[d]
        nj = sj - dj[d]
        if ni < 1 or ni >= N-1 or nj < 1 or nj >= M-1 or arr[ni][nj] == 1:
            flag = -1
        else:
            si = ni
            sj = nj

print(cnt)
