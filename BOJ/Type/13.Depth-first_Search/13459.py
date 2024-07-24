# 구슬 탈출
# 구현, 그래프이론, 그래프탐색, 너비우선탐색, 시뮬레이션

def sol(rsi, rsj, bsi, bsj, cnt):
    global result
    
    # 빨간 구슬을 넣는 경우가 있다면 종료
    if result:
        return

    # 기울인 횟수가 10번이 넘어가면 종료
    if cnt > 10:
        return

    # 4방향으로 기울이기
    for d in range(4):
        flag = 0
        rni = rsi + di[d]
        rnj = rsj + dj[d]
        bni = bsi + di[d]
        bnj = bsj + dj[d]
        if arr[rni][rnj] != '#' or arr[bni][bnj] != '#':
            # d방향으로 기울였을 때 빨간 구슬 위치
            dist1 = 0
            for c in range(1, N+M):
                rni = rsi + c*di[d]
                rnj = rsj + c*dj[d]
                if arr[rni][rnj] == '#':
                    break
                elif arr[rni][rnj] == 'O':
                    flag = 1
                    break
                elif rni == bsi and rnj == bsj:
                    continue
                else:
                    dist1 += 1
            rni = rsi + dist1*di[d]
            rnj = rsj + dist1*dj[d]

            # d방향으로 기울였을 때 파란 구슬 위치
            dist2 = 0
            for c in range(1, N+M):
                bni = bsi + c*di[d]
                bnj = bsj + c*dj[d]
                if arr[bni][bnj] == '#':
                    break
                elif arr[bni][bnj] == 'O':
                    flag = 2
                    break
                elif flag==0 and bni == rsi and bnj == rsj:
                    continue
                else:
                    dist2 += 1

            # 파란 구슬이 들어간 경우 실패
            if flag == 2:
                continue

            # 빨간 구슬만 들어간 경우 성공
            if flag == 1:
                result = 1
                return
            
            # 이동한 위치에서 다시 한 번 기울이기
            bni = bsi + dist2*di[d]
            bnj = bsj + dist2*dj[d]
            sol(rni, rnj, bni, bnj, cnt+1)


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            rsi = i
            rsj = j
        elif arr[i][j] == 'B':
            bsi = i
            bsj = j

result = 0
sol(rsi, rsj, bsi, bsj, 1)

print(result)