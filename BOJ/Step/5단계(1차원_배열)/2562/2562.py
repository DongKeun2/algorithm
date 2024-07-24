# 최댓값

X = list()
for i in range(9):
    N =int(input())
    X.append(N)
x = X[0]
c =1
for i in range(9):
    if X[i] > x:
        x = X[i]
        c = i+1
print(x)
print(c)