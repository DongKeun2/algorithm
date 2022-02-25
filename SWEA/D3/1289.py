# 원재의 메모리 복구하기

T = int(input())

for test_case in range(1, T+1):
    B = input()

    result = 0
    flag = 0
    for b in B:
        if b == '1' and flag == 0:
            result += 1
            flag = 1
        if b == '0' and flag == 1:
            result += 1
            flag = 0
    
    print(f'#{test_case} {result}')

