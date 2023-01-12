# 거짓말
# 30616KB, 40ms

N, M = map(int, input().split())

lst = list(map(int, input().split()))
lst.pop(0)

# vst에 진실을 알고 있는 사람 저장
vst = [0] * (N+1)
for n in lst:
    vst[n] = 1

# 파티 정보를 arr에 저장
arr = []
for _ in range(M):
    party = list(map(int, input().split()))
    party.pop(0)
    arr.append(party)

# 진실을 알고 있는 사람이 있는 파티를 제거
while True:
    cnt = 1
    tmp = []

    # 바로 제거하면 인덱스에 문제가 생기므로 tmp에 제거할 파티번호 기록
    # 진실을 알고 있는 사람이 있는 파티의 모든 참가자는 진실을 알게 되므로 vst 갱신
    # 진실을 아는 사람이 없을때까지 지운 뒤 남은 파티의 수 출력
    for i in range(len(arr)):
        for p in arr[i]:
            if vst[p]:
                cnt = 0
                for p in arr[i]:
                    vst[p] = 1
                tmp.append(i)
                break
    for i in tmp[::-1]:
        arr.pop(i)
    
    if cnt:
        result = (len(arr))
        break

print(result)