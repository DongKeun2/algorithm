# 좌표 압축

N = int(input())

list_num = list(map(int, input().split()))

list_2 = list(set(list_num))

list_2.sort()

for i in range(len(list_2)):
    for j in range(len(list_num)):
        if list_2[i] == list_num[j]:
            list_num[j] = str(i)

print(' '.join(list_num))
