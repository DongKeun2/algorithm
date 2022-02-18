# 정곤이의 단조 증가하는 수

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    result = -1

    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            mk = 0
            for k in str(lst[i]*lst[j]):
                if int(k) < mk:
                    break
                else:
                    mk = int(k)
            else:
                if result < lst[i]*lst[j]:
                    result = lst[i]*lst[j]

    print(f'#{test_case} {result}')