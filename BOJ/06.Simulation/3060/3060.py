# 욕심쟁이 돼지
# 구현 수학 시뮬레이션

T = int(input())

for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))

    result = [x for x in lst]
    day = 1
    while sum(result) <= N:
        for i in range(6):
            result[i] = lst[i] + lst[(i+1)%6] + lst[(i+5)%6] + lst[(i+3)%6]

        lst = [x for x in result]
        day += 1
    
    print(day)