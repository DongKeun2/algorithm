# 평균값 구하기

T = int(input())
for i in range(1, T+1):
    sum = 0
    num = list(map(int, input().split()))
    for k in num:
        sum += k
    avg = round(sum/len(num))
    print(f'#{i} {avg}')