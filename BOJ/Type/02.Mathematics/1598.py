# 꼬리를 무는 숫자 나열
# 수학, 사칙연산

a, b = map(int, input().split())
print(abs((a-1)//4 - (b-1)//4)+abs((a%4 if a%4 else 4) - (b%4 if b%4 else 4)))