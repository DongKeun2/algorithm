# 영어 끝말잇기 Lv2
# Summer/Winter Coding(~2018)

# 현재 순서인 사람이 말해야 할 첫 글지 tmp
# 나왔던 단어를 저장하는 dct
# 조건에 맞게 진행되는 지 확인
def solution(n, words):
    dct = {}
    answer = [0, 0]
    tmp = words[0][0]
    for i in range(len(words)):
        if words[i] in dct or tmp != words[i][0] or len(words) == 1:
            answer = [i%n+1, i//n+1]
            break
        else:
            tmp = words[i][-1]
            dct[words[i]] = 1

    return answer