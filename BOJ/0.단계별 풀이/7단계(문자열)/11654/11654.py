# 아스키 코드

char = input()

if type(char) == str:
    print(ord(char))
else:
    print(chr(int(char)))