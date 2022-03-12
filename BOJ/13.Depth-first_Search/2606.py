# 바이러스
# 너비우선탐색, 깊이우선탐색, 그래프 탐색, 그래프 이론

N = int(input())
K = int(input())

# arr에 길을 만들어 줌
# ex) 1 3의 경우 1=>3 3=>1 // arr[1]에 3 추가, arr[3]에 1 추가
arr = [[] for _ in range(N+1)]
for _ in range(K):
    lst = list(map(int, input().split()))
    arr[lst[1]].append(lst[0])
    arr[lst[0]].append(lst[1])

# 방문 배열
vst = [0 for _ in range(N+1)]

# 처음 1에서 시작
st = [1]
vst[1] = 1

while st:
    n = st.pop()

    # 1에 연결된 곳 감염, st에 추가
    for i in arr[n]:
        if vst[i] == 0:
            vst[i] = 1
            st.append(i)

# 1은 제외하고 바이러스 감염된 수 출력
vst[1] = 0
print(sum(vst))
