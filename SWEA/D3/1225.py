# [SW 문제해결 기본] 7일차 - 암호생성기

def sol():
    n = 1
    while lst[-1] > 0:
        num = lst.pop(0)
        lst.append(num - n)
        n = n%5+1

    lst[-1] = 0
    return

T = 10
for test_case in range(1, T+1):
    tc = int(input())
    lst = list(map(int, input().split()))

    sol()
    print(f'#{test_case}', *lst)
