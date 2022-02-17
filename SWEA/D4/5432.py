# 쇠막대기 자르기

T = int(input())

for test_case in range(1, T+1):
    n = input()

    cnt = 0
    result = 0
    for i in range(len(n)):
        if n[i] == '(':
            cnt += 1
        else:
            if n[i-1] == ')':
                cnt -= 1
                result += 1

            else:
                cnt -= 1
                result += cnt

    print(f'#{test_case} {result}')
    