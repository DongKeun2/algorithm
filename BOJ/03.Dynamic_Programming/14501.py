# 퇴사
# 다이나믹프로그래밍, 브루트포스

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N)]

# dp에 값 채우기
for i in range(N)[::-1]:
    # 상담이 가능한 경우, 최댓값 저장
    if i + arr[i][0] <= N:
        # 해당 상담이 마지막 날까지 이어지는 경우
        if i + arr[i][0] == N:
            # 마지막 날이라면 그 값을 저장
            if i == N-1:
                dp[i] = arr[i][1]
            else:
                dp[i] = max(arr[i][1], dp[i+1])

        # 이 문제에서 가장 기본적인 dp 저장 방식
        else:
            dp[i] = max(arr[i][1] + dp[i+arr[i][0]], dp[i+1])

    # 상담 불가능한 경우
    # 마지막날이라면 0으로 남기고 나머지는 다음날 상담값을 가져옴
    else:
        if i != N-1:
            dp[i] = dp[i+1]
print(max(dp))
