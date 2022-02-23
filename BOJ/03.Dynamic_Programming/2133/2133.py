# 타일 채우기

N = int(input())

if N%2:
    result = 0
else:
    dp = [0] * (N+1)
    dp[2] = 3
    for i in range(4, N+1, 2):
        dp[i] = 3*dp[i-2] + 2
        if i != 4:
            # for j in range(4, i-1, 2):
            #     dp[i] += 2*dp[j-2]
            for j in range(i-2, 3, -2):
                dp[i] += 2*dp[j-2]
    result = dp[N]

print(result)
