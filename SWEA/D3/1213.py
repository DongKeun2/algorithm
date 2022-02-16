# [S/W 문제해결 기본] 3일차 - String

T = 10

for _ in range(T):
    test_case = int(input())
    word = input()
    sent = input()
    result = 0
    for i in range(0, len(sent)- len(word) + 1):
        if word == sent[i:i+len(word)]:
            result += 1

    print(f'#{test_case} {result}')
