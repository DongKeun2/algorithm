# 후위 표기식

word = input()

result = ''
st = []
for s in word:
    if 65 <= ord(s) <= 90:
        result += s
    elif s == '(':
        st.append(s)
    elif (s == '+') or (s == '-'):
        if st:
            while st and ((st[-1] == '*') or (st[-1] == '+') or (st[-1] == '/') or (st[-1] == '-')):
                result += st.pop()
            st.append(s)
        else:
            st.append(s)
    elif (s == '*') or (s == '/'):
        if st:
            while st and ((st[-1] == '*') or (st[-1] =='/')):
                result += st.pop()
            st.append(s)
        else:
            st.append(s)
    
    else:
        while st[-1] != '(':
            result += st.pop()
        st.pop()

for x in st[::-1]:
    result += x

print(result)





