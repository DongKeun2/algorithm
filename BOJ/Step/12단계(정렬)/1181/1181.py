# 단어 정렬

N = int(input())

words = []
for _ in range(N):
    words.append(input())
set_words = set(words)
words = list(set_words)
words.sort()
max_len = 0
for word in words:
    if max_len < len(word):
        max_len = len(word)

cnt = 1
while cnt <= max_len:
    for i in range(len(words)):
        if len(words[i]) == cnt:
            print(words[i])         
    cnt += 1