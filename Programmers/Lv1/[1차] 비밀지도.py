# [1차] 비밀지도 Lv1
# 2018 KAKAO BLIND RECRUITMENT

# answer을 공백으로 n*n 배열로 초기화
# arr1, arr2에 대해 2진수로 변환, n의 길이에 맞춘다.
# s1, s2에 대해 둘 중 1인 자리를 #으로 바꾼다.
# 붙여서 반환
def solution(n, arr1, arr2):
    answer = [[' ']*n for _ in range(n)]
    for i in range(n):
        s1 = bin(arr1[i]).lstrip('0b')
        s2 = bin(arr2[i]).lstrip('0b')
        
        s1 = '0'*(n-len(s1)) + s1
        s2 = '0'*(n-len(s2)) + s2
        for j in range(n):
            if int(s1[j]) or int(s2[j]):
                answer[i][j] = '#'
    
    for i in range(n):
        answer[i] = ''.join(answer[i])
    return answer