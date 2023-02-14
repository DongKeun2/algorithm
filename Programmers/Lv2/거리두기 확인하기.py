# 2021 카카오 채용연계형 인턴십 Lv2

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
def solution(places):
    # 대기실 상태 확인
    # 앉아있는 경우 맨해튼 거리 2만큼 확인하여 사람이 있는 지 판별
    def sol(place):
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    q = [(i, j)]
                    for d in range(4):
                        ei = i + di[d]
                        ej = j + dj[d]
                        if 0 <= ei < 5 and 0 <= ej < 5:
                            if place[ei][ej] == 'O':
                                q.append((ei, ej))
                            elif place[ei][ej] == 'P':
                                return 0
                    while q:
                        si, sj = q.pop()
                        for d in range(4):
                            ei = si + di[d]
                            ej = sj + dj[d]
                            if (ei != i or ej != j) and 0 <= ei < 5 and 0 <= ej < 5:
                                if place[ei][ej] == 'P':
                                    return 0
        return 1
    
    # 모든 대기실 하나씩 확인
    answer = []
    for place in places:
        answer.append(sol(place))
                            
    return answer