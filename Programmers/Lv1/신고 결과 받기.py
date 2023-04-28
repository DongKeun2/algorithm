# 신고 결과 받기 Lv1
# 2022 KAKAO BLIND RECRUITMENT

# user인덱스 user에 저장
# rpt에 신고당한 유저 : {신고한 유저} 형태로 저장
# rpt를 돌면서 신고한 유저 수가 k 이상인 경우
# 신고한 유저들의 결과 메일 수 +1
def solution(id_list, report, k):
    n = len(id_list)
    user = {}
    rpt = {}
    for i in range(n):
        user[id_list[i]] = i
        
    for S in report:
        s, e = S.split()
        if user[e] in rpt:
            rpt[user[e]].add(user[s])
        else:
            rpt[user[e]] = set([user[s]])
            
    answer = [0] * n
    for _, ul in rpt.items():
        if len(ul) >= k:
            for u in ul:
                answer[u] += 1
    return answer