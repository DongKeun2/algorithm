# 후위 표기식2

N = int(input())
word = input()
num = []
for _ in range(N):
    num.append(int(input()))

st = []
for w in word:
    if 65 <= ord(w) <= 90:
        st.append(num[ord(w) - 65])
        
    else:
        n1 = st.pop()
        n2 = st.pop()
        if w == '+':
            st.append(n2 + n1)
        elif w == '-':
            st.append(n2 - n1)
        elif w == '*':
            st.append(n2 * n1)
        else:
            st.append(n2 / n1)

print(f'{st[0]:.2f}')
