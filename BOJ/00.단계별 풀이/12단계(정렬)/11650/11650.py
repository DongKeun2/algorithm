# 좌표 정렬하기

N = int(input())

nl = []
for _ in range(N):
    X= list(map(int, input().split()))
    nl.append(X)

nl.sort()

for n in nl:
    print(' '.join(str(x) for x in n))