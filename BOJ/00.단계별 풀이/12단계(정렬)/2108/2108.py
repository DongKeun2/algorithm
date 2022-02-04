# 통계학

N = int(input())

n_list = []
for _ in range(N):
    n_list.append(int(input()))

print(round(sum(n_list)/len(n_list)))
print(sorted(n_list)[int(len(n_list)/2)])

max_list = []
max_cnt = 0
n_set = set(n_list)
for i in n_set:
    if max_cnt < n_list.count(i):
        max_cnt = n_list.count(i)
        max_list = [i]
    elif max_cnt == n_list.count(i):
        max_list.append(i)

if len(max_list) == 1:
    print(max_list[0])
else:
    max_list.sort()
    print(max_list[1])


print(max(n_list)-min(n_list))