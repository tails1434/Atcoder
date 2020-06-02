def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    if A[0] >= 2:
        print(-1)
        exit()
    if A[0] == 1:
        if len(A) == 1:
            print(1)
            exit()



        else:
            print(-1)
            exit()
    B[0] = 1
    ans = 1
    for i in range(1,N+1):
        tmp = 2 * (B[i-1] - A[i-1])
        if tmp < A[i]:
            print(-1)
            exit()
        elif tmp == A[i]:
            if i != N:
                print(-1)
                exit()

        B[i] = tmp
    ans += A[N]
    C = [0] * (N+1)

    C[N] += A[N]
    for i in range(N-1,0,-1):
        
        if C[i+1] + A[i] <= B[i]:
            ans += A[i] + C[i+1]
            C[i] = A[i] + C[i+1]
        else:
            ans += B[i]
            C[i] = B[i]
            
    print(ans)
        







if __name__ == "__main__":
    main()