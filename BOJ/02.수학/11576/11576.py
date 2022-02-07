# Base Conversion

a, b = map(int, input().split())
m = int(input())
al = list(map(int, input().split()))

num = 0
for i in range(m):
    num += al[-(i+1)] * (a**i)

bl = []

while num != 0:
    x = num%b
    bl.append(x)
    num = num//b

print(*bl[::-1])