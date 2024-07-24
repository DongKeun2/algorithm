# 설탕 배달

N = int(input())

x = range(0, 1001)
y = range(0, 1667)

num_list = []
for i in x:
    for k in y:
        if N == (5*i + 3*k):
            num_list.append(i+k)
if bool(num_list) == False:
    print(-1)
else:
    print(min(num_list))
