# 2xn 타일링 2

n = int(input())

nl = [0] * (n+1)
nl[0] = nl[1] = 1
for i in range(2, n+1):
    nl[i] = nl[i-1] + 2*nl[i-2]

print(nl[n]%10007)