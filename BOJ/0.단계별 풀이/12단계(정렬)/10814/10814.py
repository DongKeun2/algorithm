# 나이순 정렬

N = int(input())

user_list = []

for _ in range(N):
    user_list.append(list(map(str, (input().split()))))


min_age = 9999
for user in user_list:
    if int(user[0]) < min_age:
        min_age = int(user[0])

max_age = 0
for user in user_list:
    if int(user[0]) > max_age:
        max_age = int(user[0])

cnt = int(min_age)
while cnt <= int(max_age):
    for i in range(len(user_list)):
        if int(user_list[i][0]) == cnt:
            print(' '.join(user_list[i]))
    cnt += 1