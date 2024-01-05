# 균형잡힌 세상 / 실버4
import sys
input = sys.stdin.readline

dct = {
    '(': ')',
    ')': '(',
    '{': '}',
    '}': '{',
    '[': ']',
    ']': '[',
}

while True:
    str = input().rstrip()
    if str == '.':
        break
    st = []
    for x in str:
        if x in dct:
            if x in ['(', '{', '[']: st.append(x)
            elif st and st[-1] == dct[x]: st.pop()
            else:
                st.append(x)
                break 
    print('no' if st else 'yes')