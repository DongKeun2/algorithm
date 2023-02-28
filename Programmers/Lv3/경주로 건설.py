# 경주로 건설 Lv3
# 2020 카카오 인턴십

from heapq import heappush, heappop

# 우, 하, 좌, 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
def solution(board):
    # 다익스트라 풀이
    # 0,0에 0 저장
    n = len(board)
    arr = [[10**18]*n for _ in range(n)]
    arr[0][0] = 0    
    
    # 0,1 1,0을 갈 수 있다면 힙에 추가
    # 직진비용 100, 방향저장
    h = []
    if board[0][1] == 0:
        arr[0][1] = 100
        heappush(h, (100, 0, 1, 0))
    if board[1][0] == 0:
        arr[1][0] = 100
        heappush(h, (100, 1, 0, 1))
    while h:
        sm, si, sj, sd = heappop(h)
        for d in range(4):
            if d != (sd+2)%4:
                ei = si + di[d]
                ej = sj + dj[d]
                if 0 <= ei < n and 0 <= ej < n and board[ei][ej] == 0:
                    if sd == d:
                        em = sm + 100
                    else:
                        em = sm + 600
                    
                    # 24번 테스트 케이스
                    # 해당 지점에서 비용차이가 있더라도 이후 코너 여부에 따라
                    # 500원의 차이가 발생할 수 있음
                    if em <= arr[ei][ej] + 500:
                        arr[ei][ej] = min(arr[ei][ej], em)
                        heappush(h, (em, ei, ej, d))
    answer = arr[-1][-1]
    return answer