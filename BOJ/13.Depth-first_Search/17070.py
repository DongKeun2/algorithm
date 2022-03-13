# 파이프 옮기기 1
# 그래프이론, 다이나믹프로그래밍

# 시간초과...  => dp로 다시 풀기

# dfs
def sol(i, j, flag):
    global cnt
    # 끝에 도착하면 결과값 1 증가
    if i == N-1 and j == N-1:
        cnt += 1
        return
    
    # 가로 세로 끝 부분에서 더 이상 못 가는 상태라면 종료
    elif i == N-1 and flag == 1:
        return
    elif j == N-1 and flag == 0:
        return

    # 전진
    else:
        # 가로 : 가로 and 대각선 이동
        if flag == 0:
            if j+1 < N and arr[i][j+1] == 0:
                sol(i, j+1, 0)
            if i+1 < N and j+1 < N and arr[i+1][j+1] == 0 and arr[i][j+1] == 0 and arr[i+1][j] == 0:
                sol(i+1, j+1, 2)

        # 세로 : 세로 and 대각선 이동
        elif flag == 1:
            if i+1 < N and arr[i+1][j] == 0:
                sol(i+1, j, 1)
            if i+1 < N and j+1 < N and arr[i+1][j+1] == 0 and arr[i][j+1] == 0 and arr[i+1][j] == 0:
                sol(i+1, j+1, 2)

        # 대각선 : 가로 amd 세로 and 대각선 이동
        else:
            if j+1 < N and arr[i][j+1] == 0:
                sol(i, j+1, 0)
            if i+1 < N and arr[i+1][j] == 0:
                sol(i+1, j, 1)
            if i+1 < N and j+1 < N and arr[i+1][j+1] == 0 and arr[i][j+1] == 0 and arr[i+1][j] == 0:
                sol(i+1, j+1, 2)
        return

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 첫 시작
flag = 0
i = 0
j = 1
cnt = 0
sol(i, j, flag)

print(cnt)