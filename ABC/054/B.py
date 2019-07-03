N, M = map(int, input().split())
A = []
B = []
for _ in range(N):
    A.append(input())
for _ in range(M):
    B.append(input())

for i in range(N - M + 1):
    for j in range(N - M + 1):
        flag = True

        for x in range(M):
            if A[j+x][i:i+M] != B[x]:
                flag = False
                break

        if flag == True:
            print('Yes')
            exit()

print('No')
        