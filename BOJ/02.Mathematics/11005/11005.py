# 진법 변환 2

n, b = list(map(int, input().split()))


result = ''
while n != 0:
    x = n%b
    if x <10:
        y = str(x)
    elif x >=10:
        y = chr(x+55)
      
    result = y + result
    n = n//b

print(result)