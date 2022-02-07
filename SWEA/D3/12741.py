# 두 전구

T = int(input())

result = []
for i in range(1, T+1):
    a, b, c, d = map(int, input().split())
    t = min(b, d) - max(a, c)
    if t > 0:
        result.append(t)
    else:
        result.append(0)

for i in range(1, T+1):
    print(f'#{i} {result[i-1]}')