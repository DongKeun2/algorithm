# 돌 게임

N = int(input())

# lst에 돌의 개수에 따른 승자 저장
# 돌의 개수가 1, 2, 3개 일 경우 승자는 1 2 1
lst = [0] * (N+1)
lst[1] = 1
if N >= 2:
    lst[2] = 2
if N >= 3:
    lst[3] = 1

# 경기는 항상 1번 유저가 시작
# 1개 또는 3개의 돌을 뺐을 때 2번 유저가 그 개수로 처음 시작한다고 생각할 수 있음
# 선택권은 1번 유저에게 있으므로 1개 또는 3개를 뺏을 때의 돌로 시작한다고 가정하면
# 2번 유저가 무조건 이기는 경우가 1번 유저가 무조건 이기는 경우로 바뀜
for i in range(4, N+1):
    if lst[i-1] == 2 or lst[i-3] == 2:
        lst[i] = 1
    else:
        lst[i] = 2

if lst[N] == 1:
    result = 'SK'
else:
    result = 'CY'
print(result)