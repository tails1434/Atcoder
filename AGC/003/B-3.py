def main():
    N = int(input())
    A = list(int(input()) for _ in range(N))
    cnt = 0
    for i in range(N):
        if i == N-1:
            cnt += A[i] // 2
            break
        cnt += A[i] // 2
        mod = A[i] % 2
        if A[i+1] >= mod:
            cnt += mod
            A[i+1] -= mod

    print(cnt)



if __name__ == "__main__":
    main()