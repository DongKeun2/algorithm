# 수 이어가기

n = int(input())

m = [x for x in range(n+1)]
mc = 0
for x in m:
    k = n
    cnt = 0
    ml = []
    while k >= 0:
        ml.append(k)
        k, x = x, k-x
        cnt += 1

    if mc < cnt:
        mc = cnt
        result = ml

print(mc)
print(*result)