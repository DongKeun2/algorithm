# 숫자 카드 2 / 실버4

N = int(input())
nlst = list(map(int, input().split()))
M = int(input())
mlst = list(map(int, input().split()))

dct = {}
for n in nlst:
    if n in dct:
        dct[n] += 1
    else:
        dct[n] = 1

print(*[dct[x] if x in dct else 0 for x in mlst])