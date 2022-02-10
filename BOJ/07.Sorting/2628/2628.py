# 종이자르기

N, M = map(int, input().split())

nl = [1] * (N)
ml = [1] * (M)
nl.append(0)
ml.append(0)

C = int(input())
for _ in range(C):
    a, b = map(int,input().split())
    if a == 0:
        ml[b] = 0
    else:
        nl[b] = 0

cn = []
cm = []
cnt = 0
for i in range(1, N+1):
    cnt += 1
    if nl[i] == 0:
        cn.append(cnt)
        cnt = 0

for i in range(1, M+1):
    cnt += 1
    if ml[i] == 0:
        cm.append(cnt)
        cnt = 0

ma = 0
for m in cm:
    for n in cn:
        if ma < m*n:
            ma = m*n

print(ma)