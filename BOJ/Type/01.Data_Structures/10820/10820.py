# 문자열 분석

import sys
input = sys.stdin.readline

while 1:
        word = input()
        if not word:
            break

        st = [0] * 4
        for s in word:
            if s.isupper():
                st[1] += 1
            elif s.islower():
                st[0] += 1
            elif s == ' ':
                st[3] += 1
            elif s.isdigit():
                st[2] += 1

        print(*st)
