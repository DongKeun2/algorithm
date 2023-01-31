# 코테 연습문제
# Lv3

def solution(scores):
    n, m = scores[0][0], scores[0][1]
    cnt, max_score = 0, 0

    # 태도 점수 큰 순, 평가 점수 작은 순
    scores.sort(key = lambda x : (-x[0], x[1])) 
    for i in range(len(scores)):
        if n < scores[i][0] and m < scores[i][1]:
            answer = -1
            break
        
        # 완호보다 큰 점수만 확인하며
        # 가장 큰 평가점수(index 1)를 기록하며 그것보다 작다면 pass
        elif n+m < sum(scores[i]):
            if scores[i][1] >= max_score:
                cnt += 1
            if max_score < scores[i][1]:
                max_score = scores[i][1]
    else:
        answer = cnt + 1
    return answer