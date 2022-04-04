# 트리의 높이와 너비
# pypy 통과

# 전위 순회, arr에 각 인덱스 별로 (높이, x좌표) 기록
def sol(s):
    global x

    h = arr[s][0]
    if s != -1:
        if ch1[s] != -1:
            arr[ch1[s]][0] = h+1
        if ch2[s] != -1:
            arr[ch2[s]][0] = h+1
        sol(ch1[s])
        arr[s][1] = x
        x += 1
        sol(ch2[s])

N = int(input())

arr = [[0, 0] for _ in range(N+1)]
ch1 = [0 for _ in range(N+1)]
ch2 = [0 for _ in range(N+1)]

for _ in range(N):
    a, b, c = map(int, input().split())
    ch1[a] = b
    ch2[a] = c

# 루트 정점 s 찾기
flag = 1
idx = 1
while flag:
    for i in range(1, N+1):
        if ch1[i] == idx or ch2[i] == idx:
            idx += 1
            break
    else:
        s = idx
        flag = 0

# s의 높이를 1로 나머지 좌표 찾기
arr[s][0] = 1
x = 1
sol(s)


# 최대 너비 result2 그 때의 높이 result1
result1 = 0
result2 = 0

# arr를 정렬시켜 각 높이마다 너비찾기
h = arr[s][0]
x = arr[s][1]
arr.sort()
for i in range(1, len(arr)):
    if h == arr[i][0]:
        if result2 < arr[i][1] - x + 1:
            result2 = arr[i][1] - x + 1
            result1 = h
    else:
        x = arr[i][1]
        h += 1

print(result1, result2)