# Euclid, 브론즈1

a, b = map(int, input().split())

def gcd(a, b):
    while b != 0: a, b = b, a%b
    return a

print(gcd(a, b))