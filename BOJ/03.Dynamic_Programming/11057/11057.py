# 오르막 수

n = int(input())

dp = [1] * 10
while n > 1:
    for i in range(1,10)[::-1]:
        dp[i] = sum(dp[0:i+1])
    n -= 1

print(sum(dp)%10007)
