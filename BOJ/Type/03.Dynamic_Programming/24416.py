# 알고리즘 수업 - 피보나치 수 1

# 동적 프로그래밍으로 n의 피보나치 수 구하기
def sol1(n):
    global result2

    dp = [0] * (n+1)
    dp[0] = dp[1] = dp[2] = 1

    for i in range(3, n+1):
        result2 += 1
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]


def sol2(n):
    return n-2


n = int(input())

# result2 값은 사실상 n-2
result2 = 0
result1 = sol1(n)

print(result1, result2)
