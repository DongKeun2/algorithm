# 카드 구매하기

N = int(input())
P = list(map(int, input().split()))

pl = [0] * (N+1)
pl[1] = P[0]
for i in range(2, N+1):
    pl[i] = P[i-1]
    for j in range(1, i+1):
        if pl[i] < pl[i -j] + pl[j]:
            pl[i] = pl[i-j] + pl[j]

print(pl[N])
