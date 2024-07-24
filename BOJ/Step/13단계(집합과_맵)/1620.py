# 나는야 포켓몬 마스터 이다솜
# pypy

N, M = map(int, input().split())

dct = {}
for i in range(1, N+1):
    w = input()
    dct[i] = w
    dct[w] = i

for _ in range(M):
    word = input()
    if word.isdigit():
        result = dct[int(word)]
    else:
        result = dct[word]

    print(result)