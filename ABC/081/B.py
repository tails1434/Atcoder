N = int(input())
A = list(map(int, input().split()))

count = 0
flg = True

while flg:
    for i in range(N):
        if A[i] % 2 == 0:
            A[i] = A[i] / 2
        else:
            flg = False
            print(count)
            exit()
    count += 1