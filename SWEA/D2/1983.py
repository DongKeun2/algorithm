# 조교의 성적 매기기

T = int(input())

for i in range(1, T+1):

    N, K = list(map(int, input().split()))

    list_score = []
    for _ in range(N):
        score = list(map(int, input().split()))
        list_score.append(score[0]*0.35 + score[1]*0.45 + score[2]*0.20)
    
    K_score = list_score[K-1]

    list_score.sort()

    k_rank = list_score.index(K_score) + 1

    n = N/10

    if k_rank <= n:
        result = 'D0'
    elif n < k_rank <= 2*n:
        result = 'C-'
    elif 2*n < k_rank <= 3*n:
        result = 'C0'
    elif 3*n < k_rank <= 4*n:
        result = 'C+'
    elif 4*n < k_rank <= 5*n:
        result = 'B-'
    elif 5*n < k_rank <= 6*n:
        result = 'B0'
    elif 6*n < k_rank <= 7*n:
        result = 'B+'
    elif 7*n < k_rank <= 8*n:
        result = 'A-'
    elif 8*n < k_rank <= 9*n:
        result = 'A0'
    else:
        result = 'A+'

    print(f'#{i} {result}')