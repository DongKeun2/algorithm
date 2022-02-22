# [SW 문제해결 기본] 10일차 - 비밀번호

T = 10

for test_case in range(1, T+1):
    N, n = map(str, input().split())

    lst = [x for x in n]

    i = 1
    while i < len(lst):
        if lst[i] == lst[i-1]:
            lst.pop(i)
            lst.pop(i-1)
            i -= 1
        else:
            i += 1

    result = ''.join(str(x) for x in lst)
    print(f'#{test_case} {result}')
