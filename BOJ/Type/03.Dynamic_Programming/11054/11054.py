# 가장 긴 바이토닉 부분 수열

n = int(input())
lst = list(map(int, input().split()))

dp1 = [0 for _ in range(n)]
dp2 = [0 for _ in range(n)]

dp1[0] = dp2[-1] = 1
for i in range(1, n):
    idx1 = i
    for j in range(i):
        if lst[i] > lst[j] and dp1[idx1] <= dp1[j]:
            idx1 = j
    
    dp1[i] = dp1[idx1] + 1

for i in range(n-1)[::-1]:
    idx2 = i
    for j in range(i+1, n):
        if lst[i] > lst[j] and dp2[idx2] <= dp2[j]:
            idx2 = j
    
    dp2[i] = dp2[idx2] + 1

result = [0 for _ in range(n)]
for i in range(n):
    result[i] = dp1[i] + dp2[i] - 1 

print(max(result))