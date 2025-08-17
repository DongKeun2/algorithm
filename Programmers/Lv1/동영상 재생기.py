# [PCCP 기출문제] 1번 / 동영상 재생기, Lv1

def get_time_offset_seconds(time):
    m, s = map(int, time.split(':'))
    return m * 60 + s

def get_time_offset_word(time):
    minute = str(time // 60) if time // 60 >= 10 else "0" + str(time // 60)
    second = str(time % 60) if time % 60 >= 10 else "0" + str(time % 60)
    return "{}:{}".format(minute, second)

def solution(video_len, pos, op_start, op_end, commands):
    end_time = get_time_offset_seconds(video_len)
    now_time = get_time_offset_seconds(pos)
    ops_time = get_time_offset_seconds(op_start)
    ope_time = get_time_offset_seconds(op_end)
    if ops_time <= now_time <= ope_time: now_time = ope_time

    for command in commands:
        if command == 'next':
            now_time += 10
            if now_time >= end_time: now_time = end_time
        else:
            now_time -= 10
            if now_time <= 0: now_time = 0
        if ops_time <= now_time <= ope_time: now_time = ope_time

    answer = get_time_offset_word(now_time)
    return answer