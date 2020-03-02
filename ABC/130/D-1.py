def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    right = 0
    tmp = 0
    for left in range(N):
        while tmp < K and right < N:
            tmp += A[right]
            right += 1
        if tmp >= K:
            cnt += N - right + 1
            tmp -= A[left]

    print(cnt)


if __name__ == "__main__":
    main()