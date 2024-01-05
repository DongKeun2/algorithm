# 카드2 / 실버4

N = int(input())
idx = 0
while N > 2 ** idx: idx += 1
print(2**idx if N == 2 ** idx else 2 * N % 2 ** idx)
