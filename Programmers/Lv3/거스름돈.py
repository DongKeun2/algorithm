# 거스름돈 Lv3
# 연습문제

def solution(n, money):
    money.sort()
    dp = [0] * (n+1)
    dp[0] = 1
    # 기존 dp[x]는 m을 포함시키지 않고 x원을 만든 경우
    # m원을 포함시켜 x원을 만들 수 있는 경우의 수 dp[m-x]
    for m in money:
        for x in range(m, n+1):
            dp[x] += dp[x-m]
    
    answer = dp[n]
    return answer