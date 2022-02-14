# 프리셀 통계

T = int(input())

for test_case in range(1, T+1):
    N, Pd, Pg = map(int, input().split())

    if Pd != 0 and Pg == 0:
        result = 'Broken'

    elif Pd != 100 and Pg == 100:
       result = 'Broken'

    else:
        for i in range(1, N+1):
            if (i*Pd/100) == (i*Pd//100):
                result = 'Possible'
                break
        else:
            result = 'Broken'

    print(f'#{test_case} {result}')
