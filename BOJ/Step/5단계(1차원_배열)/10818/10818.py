# 최소, 최대

N = int(input("정수의 개수 N을 입력해주세요: "))
X = list(map(int, input("정수를 입력해주세요 : "). split()))
max = X[0]
min = X[0]
for i in X[1:N]:
    if i > max:
        max = i
    elif i < min:
        min = i
print(min,max)