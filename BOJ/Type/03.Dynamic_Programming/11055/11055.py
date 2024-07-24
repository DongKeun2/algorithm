# 가장 큰 증가 부분 수열

n = int(input())
lst = list(map(int, input().split()))

dp = [lst[0]]
for i in range(1, n):
    num = 0
    for j in range(i):
        if lst[i] > lst[j] and num < dp[j]:
            num = dp[j]
    dp.append(num + lst[i])

print(max(dp))
