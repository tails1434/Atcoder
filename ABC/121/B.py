def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))

    cnt = 0
    for _ in range(N):
        A = list(map(int, input().split()))
        tmp = 0
        for i in range(M):
            tmp += A[i] * B[i]

        if tmp + C > 0:
            cnt += 1
        
    print(cnt)

main()