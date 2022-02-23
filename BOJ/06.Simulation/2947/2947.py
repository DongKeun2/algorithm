# 나무 조각

bs = list(map(int, input().split()))

i = 0
while i < 4:
    if bs[i] > bs[i+1]:
        bs[i], bs[i+1] = bs[i+1], bs[i]
        print(*bs)

    i += 1
    if i == 4 and bs != [1, 2, 3, 4, 5]:
        i = 0
