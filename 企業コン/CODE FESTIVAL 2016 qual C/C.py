def main():
    N = int(input())
    T = list(map(int, input().split()))
    A = list(map(int, input().split()))
    MOD = 10 ** 9 + 7

    ans = [0] * N
    H = [0] * N
    tmp = 0
    for i in range(N):
        if tmp < T[i]:
            tmp = T[i]
            ans[i] = 1
            H[i] = T[i]
        else:
            ans[i] = T[i]
            H[i] = T[i]

    tmp = 0
    for i in range(N-1,-1,-1):
        if tmp < A[i]:
            tmp = A[i]
            ans[i] = min(ans[i],1)
            H[i] = min(H[i],A[i])
        else:
            ans[i] = min(A[i],ans[i])
            H[i] = min(H[i],A[i])

    tmp = 0
    for i in range(N):
        tmp = max(tmp, H[i])
        if tmp != T[i]:
            print(0)
            exit()

    tmp = 0
    for i in range(N-1,-1,-1):
        tmp = max(tmp, H[i])
        if tmp != A[i]:
            print(0)
            exit()
    

    cnt = 1
    for i in ans:
        cnt *= i
        cnt %= MOD
    
    print(cnt)

if __name__ == "__main__":
    main()