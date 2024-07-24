# 덩치

N = int(input())

xl = []
for _ in range(N):
    X = list(map(int, input().split()))
    xl.append(X)

result = []

for i in xl:
    cnt = 1
    for j in xl:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    result.append(cnt)

print(' '.join(str(x) for x in result))