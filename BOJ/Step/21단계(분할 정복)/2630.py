# 색종이 만들기

def sol(tmp):
    global result1
    global result2

    n = len(tmp)

    s = 0
    for i in range(n):
        s += sum(tmp[i])

    if s == 0:
        result1 += 1
        return
    if s == n**2:
        result2 += 1
        return

    sol([lst[:n//2] for lst in tmp[:n//2]])
    sol([lst[:n//2] for lst in tmp[n//2:]])
    sol([lst[n//2:] for lst in tmp[:n//2]])
    sol([lst[n//2:] for lst in tmp[n//2:]])

N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

result1 = 0
result2 = 0
sol(arr)

print(result1)
print(result2)