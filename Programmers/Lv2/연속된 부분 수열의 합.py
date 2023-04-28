# 연속된 부분 수열의 합 Lv2
# 연습문제

# 시작지점 s부터 종료지점 i까지 확인
# tot에 해당 값을 더해간다
# tot이 k와 같다면 시작지점과 종료지점을 answer에 저장한다.
# tot이 k보다 커졌을 경우에는 시작 지점 s를 1만큼 더해준다.
# k를 만들 수 있는 모든 지점이 answer에 저장되어 있으므로
# 조건에 맞는 정렬을 통해 반환값을 결정한다. 
def solution(sequence, k):
    answer = []
    n = len(sequence)
    s = 0
    tot = 0
    for i in range(n):
        tot += sequence[i]
        while tot > k and s < i:
            tot -= sequence[s]
            s += 1
        
        if tot == k:
            answer.append((s, i))
    
    answer.sort(key=lambda x : (x[1]- x[0]))
    answer = answer[0]
    return answer