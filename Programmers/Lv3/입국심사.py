# 이분탐색 Lv3

def solution(n, times):
    answer = 0
    # 정렬 시킨 후 좌, 우 설정
    times.sort()
    start = times[0]
    end = times[0] * n

    # 이분탐색으로 n명을 심사하는 데 걸리는 최소 시간 계산
    while start < end:
        cnt = 0
        mid = (start + end) // 2
        for time in times:
            cnt += (mid//time)
        if cnt >= n:
            end = mid
        else:
            start = mid+1
    answer = start
            
    return answer