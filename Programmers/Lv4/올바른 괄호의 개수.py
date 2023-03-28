# 올바른 괄호의 갯수 Lv4
# 연습문제

# DP풀이
# ()로 감싸진 형태를 붙여서 만든다고 생각
# 만약 n=4라면
# dp[1] + (3)
# dp[2] + (2)
# dp[3] + () 와 같은 형태로 만들 수 있음
# (4)의 형태는 ((3))이므로 dp[n-1]개
# 마찬가지로 (3), (2)의 형태는 dp[2], dp[1]개와 같음
def solution(n):
    dp = [0] * 15
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    if n > 2:
        for i in range(3, n+1):
            dp[i] = dp[i-1]
            for j in range(1, i):
                dp[i] += dp[i-j]*dp[j-1]
    answer = dp[n]
    return answer