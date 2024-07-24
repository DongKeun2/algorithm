# 최대공약수와 최소공배수
import math

a, b = map(int, input().split())

c = math.gcd(a, b)
d = math.lcm(a, b)

print(c)
print(d)