# 2xn 타일링

n = int(input())

nl = [0 for i in range(n+1)]

nl[1] = nl[0] = 1
for i in range(2, n+1):
    nl[i] = nl[i-1] + nl[i-2]

print(nl[n]%10007)