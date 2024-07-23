# 문자열 폭발 / 골드4

import sys
input = sys.stdin.readline

word = input().rstrip()
target = [*input().rstrip()]
n = len(target)

st = []
for w in word:
    st.append(w)
    if w == target[-1] and st and len(st) >= n and st[-n:] == target:
        del st[-n:]

print(''.join(x for x in st) if st else 'FRULA')
