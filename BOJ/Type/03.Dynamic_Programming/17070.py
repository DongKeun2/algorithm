# 파이프 옮기기 1
# 그래프이론, 다이나믹프로그래밍

# dfs로 풀었을 때 시간 초과 => dp로 도전

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 가로, 세로, 대각선 각각 계산
dp1 = [[0 for _ in range(N)] for _ in range(N)]
dp2 = [[0 for _ in range(N)] for _ in range(N)]
dp3 = [[0 for _ in range(N)] for _ in range(N)]

# 첫 시작 (0,1) => 가로 1개 저장
dp1[0][1] = 1

# dp에 값 저장
for i in range(0, N):
    for j in range(2, N):
    	# 갈 수 잇는 곳이라면
        if arr[i][j] == 0:
        	# 세 곳 다 가능한 경우 1,2,3 모두 갱신
            if 0 <= i-1 and 0 <= j-1 and arr[i-1][j] == 0 and arr[i][j-1] == 0:
                dp1[i][j] = dp1[i][j-1] + dp3[i][j-1]
                dp2[i][j] = dp2[i-1][j] + dp3[i-1][j]
                dp3[i][j] = dp1[i-1][j-1] + dp2[i-1][j-1] + dp3[i-1][j-1]
                
            # 가로 : 왼쪽 칸에서 가로, 대각선에서 가로로 오는 경우
            # 세로 : 위 칸에서 가로, 대각선에서 세로로 오는 경우
            # 대각선 : 왼쪽 위 칸에서 가로, 세로, 대각선으로 오는 경우


			# 대각선이 불가능한 경우 1,2만 갱신
            else:
                if 0 <= i-1:
                    dp2[i][j] = dp2[i-1][j] + dp3[i-1][j]
                if 0 <= j-1:
                    dp1[i][j] = dp1[i][j-1] + dp3[i][j-1]

result = dp1[N-1][N-1] + dp2[N-1][N-1] + dp3[N-1][N-1]
print(result)
