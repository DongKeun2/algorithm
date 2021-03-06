# 스타트와 링크
# 브루트포스
# pypy 통과

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 선수 명단
lst = [0 for _ in range(N)]

# 스타트 팀 명단
st = []
for i in range(1<<N):
    team = []
    for j in range(N):
        if i & (1<<j):
            team.append(j)
    if len(team) == N//2:
        st.append(team)

# 링크 팀 명단
lt = []
for stm in st:
    team = []
    for i in range(N):
        if i not in stm:
            team.append(i)
    lt.append(team)

# 두 팀의 전력 차이 갱신
result = 2000
for i in range(len(st)):
    tot1 = 0
    for m in st[i]:
        for n in st[i]:
            if m != n:
                tot1 += arr[m][n]
    
    tot2 = 0
    for m in lt[i]:
        for n in lt[i]:
            if m != n:
                tot2 += arr[m][n]
    
    if result > abs(tot1-tot2):
        result = abs(tot1-tot2)

print(result)
