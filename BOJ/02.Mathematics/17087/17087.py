# 숨바꼭질 6

def gcd_num(a, b):
    while b != 0:
        a, b = b, a%b
    return a

N, S = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
nl = set([abs(S-a[0])])
for i in range(1, len(a)):
    nl.add(abs(S-a[i]))
    nl.add(a[i]-a[i-1])

nl = list(nl)
num = nl[0]
for i in range(len(nl)):
    num = gcd_num(num, nl[i])

print(num)