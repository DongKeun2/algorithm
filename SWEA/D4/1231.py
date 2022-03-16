# [SW 문제해결 기본] 9일차 - 중위순회

# 중위순회, 탐색한 노드의 번호를 순서대로 저장 
def sol(v):
    if v:
        sol(ch1[v])
        order.append(v)
        sol(ch2[v])
    return

T = 10
for test_case in range(1, T+1):
    N = int(input())

    # 각 노드의 왼쪽, 오른쪽 자식 입력
    # word에 각 노드 값을 입력
    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)
    word = ''
    for _ in range(N):
        lst = list(input().split())
        word += lst[1]
        if len(lst) >= 3:
            ch1[int(lst[0])] = int(lst[2])
            if len(lst) >= 4:
                ch2[int(lst[0])] = int(lst[3])

    order =[]
    v = 1
    sol(v)

    # order에 저장된 순서를 이용해 word에서 문자 가져오기
    result = ''
    for i in order:
        result += word[i-1]
    print(f'#{test_case} {result}')
