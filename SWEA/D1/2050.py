# 알파벳을 숫자로 변환

words = input()

for word in words:
    print(ord(word)-64, end= ' ')
