# 수열

N = int(input())
lst = list(map(int, input().split()))

dp1 = [1] * N
dp2 = [1] * N
for i in range(1, N):
    if lst[i] >= lst[i-1]:
        dp1[i] = dp1[i-1] +1
    if lst[i] <= lst[i-1]:
        dp2[i] = dp2[i-1] +1
    
print(max(max(dp1), max(dp2)))