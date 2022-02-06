# 좌표 정렬하기 2

N = int(input())

nl = []
for _ in range(N):
    x, y = list(map(int, input().split()))
    nl.append([y, x])

nl.sort()

for n in nl:
    print(n[1], n[0])