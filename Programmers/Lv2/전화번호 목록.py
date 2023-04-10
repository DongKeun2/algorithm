# 전화번호 목록 Lv2
# 해시

# 길이가 작은 전화번호 순으로 정렬
# 앞에서부터 확인하여 dct에 접두어로 사용될 번호가 있는 지 확인
def solution(phone_book):
    dct = {}
    phone_book.sort(key=lambda x : len(x))
    for p in phone_book:
        number = ''
        for i in range(len(p)):
            number += p[i]
            if number in dct:
                return False
        dct[p] = 1
    return True