# 문자열 집합

N, M = map(int, input().split())

S = [input() for _ in range(N)]
tmp = [input() for _ in range(M)]

result = 0
for word in tmp:
    if word in S:
        result += 1

print(result)