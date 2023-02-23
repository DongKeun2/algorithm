# 도둑질 Lv4 (스킬 레벨 테스트 Lv4에서 푼 문제)
# 동적계획법(Dynamic Programming)

# DP로 풀이
def solution(money):
    money = [0] + money
    n = len(money)

    # 집이 4개 이상이면
    if n > 4:
        dp = [[0, 0] for _ in range(n)]
        
        # 첫 집을 털거나 안 턴 경우
        dp[1][0] = money[1]
        dp[1][1] = 0

        # 이번 집을 안털거나, 턴 경우 중 큰 값 저장
        for i in range(2, len(money)-1):
            dp[i][0] = max(dp[i-1][0], dp[i-2][0] + money[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][1] + money[i])
        
        # 첫 집을 털었으면 마지막 집은 털지 않는다. 
        dp[-1][0] = dp[-2][0]
        dp[-1][1] = max(dp[-3][1] + money[-1], dp[-2][1])

        answer = max(dp[-1])
    
    # 집이 3개면 한 집만 가능
    else:
        answer = max(money)

    return answer