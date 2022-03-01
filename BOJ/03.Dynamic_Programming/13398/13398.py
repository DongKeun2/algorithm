# 연속합 2

n = int(input())
lst = list(map(int, input().split()))

result = -1000
dp1 = [0 for _ in range(n)]
dp2 = [0 for _ in range(n)]
dp1[0] = lst[0]
dp2[0] = lst[0]
for i in range(1, n):
    dp1[i] = max(lst[i], dp1[i-1] + lst[i])
    dp2[i] = max(dp1[i-1], dp2[i-1] + lst[i])
        
for i in range(n):
    result = max(result, dp1[i], dp2[i])

print(result)