# 좌표 압축

N = int(input())

nl = list(map(int, input().split()))

snl = sorted(list(set(nl)))

dnl = {}

for i in range(len(snl)):
    dnl[snl[i]] = i

result = []
for n in nl:
    result.append(dnl[n])

print(*result)
