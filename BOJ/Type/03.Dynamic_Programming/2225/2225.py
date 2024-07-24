# 합분해

n, k = map(int, input().split())

nl = [[0 for _ in range(n+1)] for _ in range(k+1)] 
for i in range(n+1):
    nl[1][i] = 1
    if k >= 2:
        nl[2][i] = i+1
if k >= 3:
    for i in range(3, k+1):
        nl[i][0] = 1
        for j in range(1, n+1):
            nl[i][j] = nl[i-1][j] + nl[i][j-1]

print(nl[k][n]%1000000000)