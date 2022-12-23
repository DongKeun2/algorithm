# 하노이 탑 이동순서

def sol(n, x, y, z):
    if n == 1:
        print(x, z)
        return
    sol(n-1, x, z, y)
    print(x, z)
    sol(n-1, y, x, z)


n = int(input())
result = 1
for i in range(n-1):
    result = result*2 + 1
print(result)
sol(n, 1, 2, 3)
