# 줄 세우기

N = int(input())

lst = [ i+1 for i in range(N) ]

cl = list(map(int, input().split()))

for i in range(N):
    num = lst.pop(i)
    lst.insert(i-cl[i], num)

print(*lst)