# 8진수 2진수

on = str(input())

tn = int('0o' + on, 8)

result = bin(tn)[2:]
print(result)