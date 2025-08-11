# 2025 프로그래머스 코드챌린지 1차 예선, lv1

# 지각 커트라인 계산 함수
def get_end_time(time):
    reminder = time // 100
    new_minute = (time % 100) + 10  
    if new_minute >= 60: new_minute += 40
    return reminder*100 + new_minute

def solution(schedules, timelogs, startday):
    answer = 0
    # 직원마다 확인
    for i in range(len(timelogs)):
        flag = True
        end_time = get_end_time(schedules[i])
        for j in range(7):
            # 주말 제외하고 확인
            if not(not (startday + j) % 7 or (startday + j) % 7 == 6):
                if timelogs[i][j] > end_time: flag = False
        if flag: answer += 1
    return answer