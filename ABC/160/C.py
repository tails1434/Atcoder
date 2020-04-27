def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    ans = float('inf')
    for i in range(N):
        if A[i] > A[i-1]:
            tmp = (K + A[i-1]) - A[i]
        else:
            tmp = A[i-1] - A[i]
        ans = min(ans, tmp)

    for i in range(N):
        if i == N - 1:
            tmp = A[i] - A[0]
        else:
            tmp = K - (A[i+1] - A[i])
        ans = min(ans, tmp)

    print(ans)



if __name__ == "__main__":
    main()