# 스킬트리 Lv2
# Summer/Winter Coding(~2018)

# dct에 상위 스킬트리 저장
# 하나의 스킬마다 확인
## 상위 스킬이 필요한지 확인
### 첫 번째 스킬이라면 바로 사용가능
### 상위 스킬이 필요하다면 상위 스킬이 tmp에 존재하는 지 확인
### 해당 스킬을 사용할 수 있다면 tmp에 저장
def solution(skill, skill_trees):
    n = len(skill)
    dct = {}
    for i in range(1, n)[::-1]:
        dct[skill[i]] = skill[i-1]
    
    answer = 0
    for skl in skill_trees:
        tmp = {}
        for s in skl:
            if s == skill[0]:
                tmp[s] = 1
            elif s in dct:
                if dct[s] not in tmp:
                    break
                else:
                    tmp[s] = 1
        else:
            answer += 1
                    
    return answer