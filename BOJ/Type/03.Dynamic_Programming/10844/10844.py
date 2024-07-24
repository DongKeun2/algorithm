# 쉬운 계단 수

N = int(input())

nl = [[0 for _ in range(10)] for _ in range(N+1)]

for i in range(1, 10):
    nl[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            nl[i][j] = nl[i-1][1]
        elif j == 9:
            nl[i][j] = nl[i-1][8]
        else:
            nl[i][j] = nl[i-1][j-1] + nl[i-1][j+1]

print(sum(nl[N])%1000000000)