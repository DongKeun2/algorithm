# 도로와 신호등

N, L = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

lst = [0 for _ in range(L+1)]

for i in range(len(arr)):
    lst[arr[i][0]] = 1

i = 0
t = 0
while i != L:
    if lst[i] == 0:
        i += 1

    t += 1
    
    for j in range(len(arr)):
        if t != 0: 
            if t%(arr[j][1]+arr[j][2]) == arr[j][1]: 
                lst[arr[j][0]] = 0
            elif t%(arr[j][1]+arr[j][2]) == 0:
                lst[arr[j][0]] = 1
    
print(t)