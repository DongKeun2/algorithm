# 요세푸스 문제0

N, K = map(int, input().split())

lst = [x for x in range(1, N+1)]
result = []

i = 0

while lst:
    N = len(lst)
    i = (i+K-1)%N
    result.append(lst.pop(i))

sol = ', '.join(str(x) for x in result)
print(f'<{sol}>')
