# 맞춰봐
# 백트래킹

# 시간초과 ...

def sol():
    global result
    check = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            tot = 0
            for k in range(i, j):
                tot += lst[k]
            check.append(tot)
    for i in range(len(check)):
        if check[i] > 0 and flag[i] == '+':
            continue
        elif check[i] < 0 and flag[i] == '-':
            continue
        elif check[i] == 0 and flag[i] == '0':
            continue
        else:
            return
    else:
        result = [x for x in lst]
        return

def dfs():
    global result
    if len(lst) >= N:
        sol()
        return
    elif result != []:
        return
    else:
        for i in range(21):
            if vst[i] == 0:
                vst[i] = 1
                lst.append(num[i])
                dfs()
                vst[i] = 0
                lst.pop()

N = int(input())
flag = list(input())
num = [x for x in range(-10,11)]
vst = [0 for _ in range(21)]
lst = []
result = []
dfs()
print(*result)