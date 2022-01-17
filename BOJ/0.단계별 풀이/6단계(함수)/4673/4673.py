# 셀프 넘버

x = set(range(1,10001))
y = set()
for i in range(1,10001):
    p = i
    while True:
        l = p%10
        m = (p%100)//10
        n = (p%1000)//100
        o = p//1000
        p = p+l+m+n+o
        if p>10000:
            break
        y.add(p)
s = sorted(x - y)
for i in s:
    print(i)
print(c)