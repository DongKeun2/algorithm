# 링크와 스타트
# 브루트포스
# pypy통과

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
    if len(team) != N:
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
    # 스타트 팀 전력
    tot1 = 0
    for m in st[i]:
        for n in st[i]:
            if m != n:
                tot1 += arr[m][n]
    # 링크 팀 전력
    tot2 = 0
    for m in lt[i]:
        for n in lt[i]:
            if m != n:
                tot2 += arr[m][n]
    # 비교 갱신
    if result > abs(tot1-tot2):
        result = abs(tot1-tot2)

print(result)
