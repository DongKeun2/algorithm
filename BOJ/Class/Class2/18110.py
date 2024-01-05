# solved.ac / 실버4

import sys, math
input = sys.stdin.readline

# 내장 round함수는 오사오입이라 오답
def round(n):
    if n * 10 % 10 >= 5:
        return math.ceil(n)
    return int(n)

n = int(input())
lst = [int(input()) for _ in range(n)]
m = round(n * 0.15)
print(round(sum(sorted(lst)[m: n-m]) / (n-2*m)) if n else 0)