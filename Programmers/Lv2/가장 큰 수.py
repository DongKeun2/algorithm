# 가장 큰 수 Lv2
# 정렬

# 4자리로 변환하여 우선순위 계산 정렬
# 0으로 시작하는 경우는 답이 0
def solution(numbers):
    numbers.sort(key=lambda x : (str(x)*4)[:4], reverse=True)
    answer = ''.join(str(x)[:len(str(x))] for x in numbers)
    answer = '0' if answer[0] == '0' else answer
    return answer