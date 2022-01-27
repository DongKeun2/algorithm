# 지그재그 숫자

T = int(input())

for i in range(1, T+1):
    N = int(input())

    total = 0
    for idx in range(1, N+1):
        if idx % 2 == 0:
            total -= idx
        else:
            total += idx

    print(f'#{i} {total}')