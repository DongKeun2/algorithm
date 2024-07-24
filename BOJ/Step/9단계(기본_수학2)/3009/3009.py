# 네 번째 점

X_1 = list(map(int, input().split()))
X_2 = list(map(int, input().split()))
X_3 = list(map(int, input().split()))

list_X = [X_1, X_2, X_3]
list_x = []
list_y = []
for i in list_X:
    list_x.append(i[0])
    list_y.append(i[1])

if list_x[0] == list_x[1]:
    x = list_x[2]
elif list_x[0] == list_x[2]:
    x = list_x[1]
else:
    x = list_x[0]

if list_y[0] == list_y[1]:
    y = list_y[2]
elif list_y[0] == list_y[2]:
    y = list_y[1]
else:
    y = list_y[0]

print(x, y)

