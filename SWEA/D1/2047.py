# 신문 헤드라인

sentence = input()

word_list = []
for i in sentence:
    if 97 <= ord(i) <= 122:
        word_list.append(str(chr(ord(i)-32)))
    else:
        word_list.append(i)
print(''.join(word_list))