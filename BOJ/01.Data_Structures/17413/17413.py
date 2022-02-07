# 단어 뒤집기 2

S = input()

st = ''
result = ''

for s in S:
    if s == '<':
        result += st[::-1]
        st = ''
        st += s
    elif s == '>':
        result += st
        result += s
        st = ''
    elif s == ' ':
        if '<' in st:
            st += s
        else:
            result += st[::-1]
            result += ' '
            st = ''
    else:
        st += s

if st != '':
    result += st[::-1]

print(result)
