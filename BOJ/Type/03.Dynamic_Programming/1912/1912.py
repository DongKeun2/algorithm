# 연속합

n = int(input())
nl = list(map(int, input().split()))

cl = [0] * n
cl[0] = nl[0]

for i in range(1, n):
    cl[i] = nl[i]
    if cl[i] < cl[i-1] + cl[i]:
        cl[i] += cl[i-1]

print(max(cl))