# 평범한 숫자

T = int(input())

for i in range(1, T+1):
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for k in range(n):
        if k == 0 and k == n-1:
            if p[k-1] < p[k] < p[k] or p[k-1] > p[k] > p[k]:
                cnt += 1

    print(f'#{i} {cnt}')