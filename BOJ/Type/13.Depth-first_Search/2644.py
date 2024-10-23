# 촌수계산
# DFS

# 1 <= n <= 100
n = int(input())
start, end = map(int, input().split())

arr = [[0] * (n + 1) for _ in range(n + 1)]
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    arr[x][y], arr[y][x] = 1, 1
    

# 초기 answer 101로 설정
answer = 101

# start에서 a까지의 거리를 저장하는 배열, start는 0으로 초기화
vst = [101] * (n + 1)
vst[start] = 0 
st = [start]
while st:
    s = st.pop()
    if s == end and answer > vst[s]:
        answer = vst[s]
    
    for e in range(1, n + 1):
        if arr[s][e] and vst[e] > vst[s] + 1:
            vst[e] = vst[s] + 1
            st.append(e)

# answer이 101이라면 -1로 변환
if answer == 101: answer = -1
print(answer)