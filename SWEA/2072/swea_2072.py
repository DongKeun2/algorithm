# 홀수만 더하기

T = int(input())
for i in range(T):
    sum = 0
    num = list(map(int, input().split()))
    for j in num:
        if j % 2 == 1:
            sum += j
    print('#{0} {1}'.format(i+1, sum))