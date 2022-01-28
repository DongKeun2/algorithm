# 쉬운 거스름돈

T = int(input())

for i in range(1, T+1):

    N = int(input())

    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    num = []
    for k in range(len(money)):
        if N >= money[k]:
            num.append(N//money[k])
            N -= (N//money[k]) * money[k]
        else:
            num.append(0)
        result = ' '.join(str(n) for n in num)

    print(f'#{i}')
    print(result)