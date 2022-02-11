# 참외밭

n = int(input())

arr = []
for i in range(6):
    arr.append(list(map(int, input().split())))

mx = 0
my = 0
xi = 0
yi = 0

for i in range(6):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if mx < arr[i][1]:
            mx = arr[i][1]
            xi = i

    elif arr[i][0] == 3 or arr[i][0] == 4:
        if my < arr[i][1]:
            my = arr[i][1]
            yi = i

area = mx * my

fx = abs(arr[(yi-1)%6][1] - arr[(yi+1)%6][1])
fy = abs(arr[(xi-1)%6][1] - arr[(xi+1)%6][1])

area -= fx*fy

print(area*n)