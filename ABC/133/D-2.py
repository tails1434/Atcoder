def main():
    N = int(input())
    A = list(map(int, input().split()))
    x = [0] * N
    for i in range(N):
        if i % 2 == 0:
            x[0] += A[i]
        else:
            x[0] -= A[i]
    for i in range(N-1):
        x[i+1] = 2 * A[i] - x[i]

    print(*x)

if __name__ == "__main__":
    main()