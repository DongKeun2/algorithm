# H - 클린알파 Lv4

import sys
input = sys.stdin.readline

P, N = map(int, input().split())
lst = list(map(int, input().split()))

# 입력받은 lst의 길이만큼 연산 (최대 10의6승)
result = 0
for num in lst:
    result *= P
    result %= 1000000007
    result += num  


# 출력에 나머지 안해도 정답처리 why?
print(result % 1000000007)