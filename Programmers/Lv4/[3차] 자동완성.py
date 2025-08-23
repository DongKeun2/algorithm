# 2018 KAKAO BLIND RECRUITMENT, [3차] 자동완성, Lv4

# Node, Trie 클래스 선언
class Node:
    def __init__(self, key, cnt = 0):
        self.child = {}
        self.key = key
        self.cnt = cnt

class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.child:
                node.child[w] = Node(w)
            node = node.child[w]
            node.cnt += 1

    def search(self, word):
        node = self.root
        cnt = 0
        for w in word:
            cnt += 1
            node = node.child[w]
            if node.cnt == 1: return cnt
        return cnt

# trie 구조로 재풀이
def solution(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    answer = 0
    for word in words:
        answer += trie.search(word)
    return answer



# 효율성 테스트 4문제 시간 초과
def solution(words):
    dct = {}
    for word in words:
        for i in range(1, len(word)+1):
            S = word[:i]
            if word[:i] in dct: dct[S] += 1
            else: dct[S] = 1

    answer = 0
    for word in words:
        cnt = 0
        for i in range(1, len(word)+1):
            S = word[:i]
            cnt += 1
            if dct[S] <= 1:
                answer += cnt
                break
        else: answer += len(word)
    return answer