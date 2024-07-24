# 창고 다각형

N = int(input())

k = 0
ll = [0]*1001
for _ in range(N):
    x, y = map(int, input().split())
    ll[x] = y
    if k < x:
        k = x

ml = max(ll)
mi = ll.index(ml)

my = 0
mx = 0
result = 0
for i in range(1, mi+ 1):
    if my < ll[i]:
        result += (i - mx) * my
        my = ll[i]
        mx = i

mx = k
my = ll[k]
for i in range(mi, k+1)[::-1]:
    if my <= ll[i]:
        result += (mx - i) * my
        my = ll[i]
        mx = i
result += ml

print(result)
