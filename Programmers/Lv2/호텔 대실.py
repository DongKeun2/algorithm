# 호텔 대실
# 연습문제 LV2

# tmp에 해당 시간에 필요한 방의 수 저장
def solution(book_time):
    tmp = [0] * ((24*60) + 10)
    for time in book_time:
        h1 = int(time[0][0:2]) * 60
        m1 = int(time[0][3:5])
        h2 = int(time[1][0:2]) * 60
        m2 = int(time[1][3:5])
        
        start = h1 + m1
        end = h2 + m2
        for i in range(start, end+10):
            tmp[i] += 1
    
    # 가장 많은 방이 필요한 시간의 값 출력
    answer = max(tmp)
    return answer