def solution(elements):
    n = len(elements)
    elements.extend(elements)
    
    # 겹치지 않게 set에 연속 부분 수열의 합 저장
    result = set()
    result.add(sum(elements))
    for i in range(n):
        tmp = elements[i]
        result.add(tmp)
        for j in range(i+1, i+n-1):
            tmp += elements[j]
            result.add(tmp)
    answer = len(result)
    return answer