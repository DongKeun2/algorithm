# 곱셈 / 실버1
# 분할 정복

def sol(a, b):
    if b == 0:
        return 1
    if b == 1:
        return ((a * b) % C) 
    return sol((a % C)** 2 % C, b // 2) * sol(a, b % 2) % C

A, B, C = map(int, input().split())
print(sol(A, B))
