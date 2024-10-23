# 다각형, 실버5

a, b = map(int, input().split())

a = a+1 if a%2 else a
b = b-1 if b%2 else b

answer = b if b == a else int((b+a)*((b-a+2)/4))
print(answer - 2 if b >= 2 >= a else answer)