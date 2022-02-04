# 에디터

word = list(input())

num = int(input())

st = []

for i in range(num):
    com = input().split()

    if com[0] == 'L':
        if word:
            st.append(word.pop())

    elif com[0] == 'D':
        if st:
            word.append(st.pop())

    elif com[0] == 'B':
        if word:
            word.pop()

    else:
        word.append(com[1])

print(''.join(s for s in (word+st[::-1])))
