# 단어 공부

word = input()

A_to_Z = range(65,91)
a_to_z = range(97,123)
list_cnt = []
for A in A_to_Z:
    cnt_A = 0
    for i in word:
        if chr(A) == i:
            cnt_A += 1
        else:
            continue
    list_cnt.append(cnt_A)
for a in range(26):
    cnt_a = 0
    for i in word:
        if chr(97+a) == i:
            cnt_a += 1
        else:
            continue
    list_cnt[a] += cnt_a

max_num = -1
for idx, k in enumerate(list_cnt):
    if k >= max_num:
        max_num = k
        idx_max = idx
    else:
        continue

cnt_max = 0   
for l in list_cnt:
    if l == max_num:
        cnt_max += 1
    else:
        continue

if cnt_max == 1:
    print(chr(65+idx_max))
else:
    print('?')