def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (2 * N)

    for i in range(2*N):
        if i < N:
            B[i] = A[i]
        else:
            B[i] = K + A[i - N]

    l = 0
    for i in range(N):
        tmp = B[i+1] - B[i]
        l = max(l, tmp)

    ans = K - l
    print(ans)



if __name__ == "__main__":
    main()