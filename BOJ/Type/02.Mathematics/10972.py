# 다음 순열
# 수학, 조합론

N = int(input())
lst = list(map(int, input().split()))

# 뒤부터 확인
for i in range(N-1)[::-1]:
    # 작아지는 부분 찾기
    if lst[i] < lst[i+1]:
        num = N

        # 그 뒤 작아지는 수보다 큰 수 중 최솟값 찾기
        for j in range(i+1, N):
            if lst[i] < lst[j] < num:
                num = lst[j]

        # 인덱스 찾아서 바꿔주기
        k = lst.index(num)
        lst[i], lst[k] = lst[k], lst[i]

        # 뒷 부분은 오름차순 정렬
        lst = lst[:i+1] + sorted(lst[i+1:])
        print(*lst)
        break

# 작아지는 부분이 없다면 -1
else:
    print(-1)