# 2진수 8진수

num = str(input())

tn = int('0b' + num, 2)
result = oct(tn)
print(result[2:])