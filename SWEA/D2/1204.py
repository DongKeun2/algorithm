# 최빈수 구하기

T = int(input())

for _ in range(1, T+1):
    i = int(input())
    list_s = list(map(int, input().split()))
    max_c = 0
    num_list = [x for x in range(0, 101)]

    for k in num_list:
        if list_s.count(k) > max_c:
            max_c = list_s.count(k)
            max_score = k
        elif list_s.count(k) == max_c:
            if k > max_score:
                max_score = k
            

    print(f'#{i} {max_score}')