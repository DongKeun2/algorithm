# 쉬운 거스름돈

T = int(input())

for i in range(1, T+1):

    N = int(input())

    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = []
    for j in range(len(money)):
        if N >= money[j]:
            result.append(N//money[j])
            N -= (N//money[j]) * money[j]
        else:
            result.append(0)


    print(f'#{i}')
    print(*result)