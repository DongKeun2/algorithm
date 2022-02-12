# 13599. [S/W 문제해결 기본] 1일차 - View

import sys

sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))
    result = 0
    for i in range(2, N-2):
        if (lst[i-2] < lst[i]) and (lst[i-1] < lst[i]) and (lst[i+1] < lst[i]) and (lst[i+2] < lst[i]):
            max_h = 0
            for j in range(i-2, i+3):
                if (i != j) and (max_h < lst[j]):
                    max_h = lst[j]
            result += (lst[i] - max_h)
    print(f'#{test_case} {result}')

