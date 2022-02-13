# 가장 긴 증가하는 부분 수열

n = int(input())

a = list(map(int, input().split()))

nl = [0] * (n)
nl[0] = 1

for i in range(1, n):
    mn = 0
    for j in range(0, i):
        if a[i] > a[j]:
            if mn < nl[j]:
                mn = nl[j]
    
    nl[i] += mn + 1

print(max(nl))