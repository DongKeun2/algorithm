# 듣보잡 /실버4

N, M = map(int, input().split())
dct = {}
for _ in range(N):
    dct[input()] = 1

result = []
for _ in range(M):
    word = input()
    if word in dct:
        result.append(word)
print(len(result))
for word in sorted(result):
    print(word)