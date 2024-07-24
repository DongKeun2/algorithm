# 카드 섞기

# 입력받기
N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))

# 카드 배열 복사
lst = [x for x in P]
lst2 = [x for x in P]

# 값 초기화
result = -1
cnt = 0

# 한 바퀴 돌 동안 답이 안나오거나 찾으면 break
while 1:

    # lst의 카드배열이 나눠줄 수 있는 배열인가?
    for i in range(N):
        if lst[i]%3 != i%3:
            break
    else:
        result = cnt
        break
    
    # 나눠줄 수 없는 배열이면 카드 배열 바꾸고 cnt += 1
    for i in range(N):
        lst2[S[i]] = lst[i]
    cnt += 1

    # lst에 lst2(바뀐 카드 배열) 복사
    lst = [x for x in lst2]

    # 만약 한 바퀴를 돌아 lst가 P(원래 카드배열)과 같아지면 종료
    if lst == P:
        break

print(result)


