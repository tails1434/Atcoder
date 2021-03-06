def main():
    N = int(input())
    A = [0] * (N + 1)
    cnt = 0
    for i in range(N):
        A[i] = int(input())

    for i in range(N):
        cnt += A[i] // 2
        A[i] %= 2

        if A[i] > 0 and A[i+1] > 0:
            cnt += 1
            A[i] -= 1
            A[i+1] -= 1

    print(cnt)


if __name__ == "__main__":
    main()