# 일곱 난쟁이

lst = [int(input()) for _ in range(9)]

result = []
for i in range(1<<len(lst)):
    cnt = 0
    result = []
    for j in range(len(lst)):
        if i & (1<<j):
            cnt += 1
            result.append(lst[j])
    if cnt == 7:
        if sum(result) == 100:
            break

result.sort()
for i in range(len(result)):
    print(result[i])