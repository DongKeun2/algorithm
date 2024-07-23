# 내려가기 / 골드5
# DP, 슬라이딩 윈도우

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
dp = [[lst[0], lst[1], lst[2]], [lst[0], lst[1], lst[2]]]
for _ in range(N-1):
    lst = list(map(int, input().split()))
    dp[0] = [lst[0] + max(dp[0][0], dp[0][1]), lst[1] + max(dp[0]), lst[2] + max(dp[0][1], dp[0][2])]
    dp[1] = [lst[0] + min(dp[1][0], dp[1][1]), lst[1] + min(dp[1]), lst[2] + min(dp[1][1], dp[1][2])]
print(max(dp[0]), min(dp[1]))