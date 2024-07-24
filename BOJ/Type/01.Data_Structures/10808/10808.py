# 알파벳 개수

S = input()

nl = [i for i in range(97, 123)]

st = []
for n in nl:
    st.append(S.count(chr(n)))

print(*st)
