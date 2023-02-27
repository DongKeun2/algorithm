# 베스트앨범 Lv3
# 해시 

# 장르 : (총횟수, [(횟수, 고유번호)])
def solution(genres, plays):    
    n = len(genres)
    dct = {}
    for i in range(n):
        g = genres[i]
        p = plays[i]
        if g in dct:
           dct[g][0] += p
           dct[g][1].append((p, i))
        else:
            dct[g] = [p, [(p, i)]]

    # 총 횟수를 기준으로 장르 순서 정렬
    # 각 장르별로 가장 재생 횟수가 높은 노래 2개 선택
    tmp = {v[0]:k for k, v in dct.items()}
    answer = []
    for x in sorted(tmp.keys(), reverse=True):
        dct[tmp[x]][1].sort(key=lambda x : (x[0], -x[1]), reverse=True)
        answer.append(dct[tmp[x]][1][0][1])
        if len(dct[tmp[x]][1]) >= 2:
            answer.append(dct[tmp[x]][1][1][1])
    return answer