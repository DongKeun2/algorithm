# 그룹 단어 체커

N = int(input())

cnt = N
for i in range(N):
    word = input()
    if len(word) >= 3:
        for x in range(2,len(word)):
            cnt_x = 0
            if word[x] != word[x-1]:
                if word[x] in word[:x]:
                    cnt_x -= 1
                    break
        if cnt_x < 0:
            cnt -=1

print(cnt)