# 스티커 모으기(2) Lv3
# Summer/Winter Coding(~2018)

# 다이나믹 프로그래밍 풀이, 3차원 list활용
# 3개 이하의 스티커는 하나만 선택할 수 있음
# 4개 이상일 경우
## 첫 번째 스티커를 선택한 경우와 아닌 경우로 분리
### 해당 스티커를 포함하냐 아니냐로 분류

# 마지막 스티커는 첫 번째 스티커를 포함한 경우에는 절대 포함할 수 없음
## 첫 번째 스티커를 포함하지 않은 경우에는 마지막 스티커를 포함할 수 있음
def solution(sticker):
    n = len(sticker)
    # 첫 번째를 포함하냐, 해당 스티커를 포함하냐
    dp = [[[0, 0] for _ in range(2)] for _ in range(n)]
    dp[0][0][0] = sticker[0]
    if n > 3:
        dp[1][1][0] = sticker[1]
        for i in range(2, n-1):
            dp[i][0][0] = max(max(dp[i-2][0]), dp[i-1][0][1]) + sticker[i]
            dp[i][0][1] = max(max(dp[i-2][0]), max(dp[i-1][0]))
            dp[i][1][0] = max(max(dp[i-2][1]), dp[i-1][1][1]) + sticker[i]
            dp[i][1][1] = max(max(dp[i-2][1]), max(dp[i-1][1]))
        dp[n-1][0][0] = max(max(dp[n-3][0]), max(dp[n-2][0]))
        dp[n-1][0][1] = max(max(dp[n-3][0]), max(dp[n-2][0]))
        dp[n-1][1][0] = max(max(dp[n-3][1]), dp[n-2][1][1]) + sticker[n-1]
        dp[n-1][1][1] = max(max(dp[n-3][1]), max(dp[n-2][1]))
    else:
        return max(sticker)
    
    answer = max(max(dp[-1][0]), max(dp[-1][1]))
    return answer