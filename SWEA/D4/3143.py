# 가장 빠른 문자열 타이핑

T = int(input())

for test_case in range(1, T+1):
    A, B = map(str, input().split())

    i = 0
    result = 0
    while i < len(A):
        if i+len(B) <= len(A) and A[i:i+len(B)] == B:
            i += len(B)
            result += 1
        else:
            i += 1
            result += 1

    print(f'#{test_case} {result}')