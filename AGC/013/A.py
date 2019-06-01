N = int(input())

A = list(map(int, input().split()))

cnt = 1
flag = 0

for i in range(1,N):
    if flag == 0:
        if A[i-1] < A[i]:
            flag = 1
        elif A[i-1] > A[i]:
            flag = -1
    if flag == 1:
        if A[i-1] > A[i]:
            flag = 0
            cnt += 1
    if flag == -1:
        if A[i-1] < A[i]:
            flag = 0
            cnt +=1

print(cnt)