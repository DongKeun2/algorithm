# 우박수열 정적분 연습문제 LV2

def solution(k, ranges):
    # tmp에 idx를 x좌표, k를 y좌표로 저장
    tmp = []
    while True:
        tmp.append(k)
        if k <= 1:
            break
        if k%2:
            k *= 3
            k += 1
        else:
            k //= 2
    
    n = len(tmp)
    answer = []
    for a, b in ranges:
        start = a
        end = n + b -1
        if start == end:
            answer.append(float(0.0))   # 시작지점과 종료지점이 같으면 0
        elif end < start:
            answer.append(float(-1.0))  # 시작지점보다 종료지점이 먼저 나오면 -1
        
        # 그렇지 않다면 구간 합 구해서 저장
        else:
            cnt = 0
            for x in range(start, end):
                cnt += max(tmp[x], tmp[x+1]) - abs(tmp[x] - tmp[x+1]) / 2
            answer.append(cnt)
            
    return answer