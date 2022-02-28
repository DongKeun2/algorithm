# 방 번호

N = int(input())

lst = [0 for _ in range(10)]

for n in str(N):
    lst[int(n)] += 1

x = lst[6]
y = lst[9]

lst[6], lst[9] = 0, 0
lst.append((x+y+1)//2)

print(max(lst))