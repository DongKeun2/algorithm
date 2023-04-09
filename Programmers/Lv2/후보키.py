# 후보키 Lv2
# 2019 KAKAO BLIND RECRUITMENT

# 딕셔너리 활용 풀이
# 후보키 후보 컬럼을 combinations으로 모두 확인, lst
# 확인하는 후보키의 부분집합 중 후보키가 있다면 건너뛰기, chk
# tmp를 활용하여 같은 값이 있는 지 문자열로 확인 <= 이 부분은 테케가 있다면 오답 가능성이 있음
# 후보키가 된다면 dct에 lst 저장 
from itertools import combinations

def solution(relation):
    n = len(relation)
    m = len(relation[0])
    arr = [_ for _ in range(1, m+1)]
    dct = {}
    for i in range(1, m+1):
        for lst in combinations(arr, i):
            flag = False
            
            for j in range(1, i+1):
                for chk in combinations(lst, j):
                    if chk in dct:
                        flag = True
                        break
                if flag:
                    break
            else:
                tmp = {}
                for k in range(n):
                    a = []
                    for l in lst:
                        a.append(relation[k][l-1])
                    if ''.join(x for x in a) in tmp:
                        break
                    else:
                        tmp[''.join(x for x in a)] = 1
                        
                else:
                    dct[lst] = 1

    answer = len(dct)
    return answer