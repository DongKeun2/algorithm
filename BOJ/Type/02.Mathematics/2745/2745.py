# 진법 변환

n, b = list(map(str, input().split()))

b = int(b)
result = 0
if b < 10:
    for i in range(len(n)):
        if int(n[-(i+1)]):
            result += int(n[-(i+1)])*(b**i)

else:
    for i in range(len(n)):
        if 65 <= ord(n[-(i+1)]) <= 90:
            x = ord(n[-(i+1)])-55
            result += x*(b**i)
        else:
            result += int(n[-(i+1)])*(b**i)

print(result)
