# 최소공배수

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    x, y = a, b
    while y > 0:
        x, y = y, x%y
    
    gcd_c = x

    lcm_d = ((a//gcd_c) * (b//gcd_c)) * gcd_c

    print(lcm_d)