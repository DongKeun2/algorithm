# 요세푸스 문제

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nl = [x for x in range(1, n+1)]
r = []
num = 0

while nl != []:
    num += k-1

    if num >= len(nl):
        num = num % len(nl)

    r.append(nl.pop(num))

result = ', '.join(str(x) for x in r)

print(f'<{result}>')