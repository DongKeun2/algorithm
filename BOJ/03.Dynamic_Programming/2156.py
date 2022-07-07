# 포도주 시식

n = int(input())

lst = [int(input()) for _ in range(n)]

if n < 3:
    result = sum(lst)
else:
    dp = [0] * n

    dp[0] = lst[0]
    dp[1] = lst[0] + lst[1]
    dp[2] = max(lst[2]+lst[1], lst[2]+lst[0], lst[1])

    for idx in range(2, n):
        dp[idx] = max(dp[idx-1], dp[idx-3]+lst[idx-1]+lst[idx], dp[idx-2]+lst[idx])

    result = dp[-1]

print(result)
