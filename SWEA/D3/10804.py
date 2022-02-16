# 문자열의 거울상

T = int(input())

for test_case in range(1, T+1):
    w = input()
    w = w[::-1]
    result = ''
    for i in range(len(w)):
        if w[i] == 'b':
            result += 'd'
        elif w[i] == 'd':
            result += 'b'
        elif w[i] == 'p':
            result += 'q'
        else:
            result += 'p'

    print(f'#{test_case} {result}')
    