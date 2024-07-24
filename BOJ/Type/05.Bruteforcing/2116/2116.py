# 주사위 쌓기

N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

on = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0}

rl = []
for i in range(6):
    mn = []
    nl = [1,2,3,4,5,6]
    nl.remove(arr[0][i])
    un = arr[0][on[i]]
    nl.remove(arr[0][on[i]])
    msn = max(nl)
    mn.append(msn)

    for j in range(1, N):
        nl = [1,2,3,4,5,6]
        nl.remove(un)
        un = arr[j][on[arr[j].index(un)]]
        nl.remove(un)
        msn = max(nl)
        mn.append(msn)
    
    rl.append(sum(mn))

result = max(rl)

print(result)