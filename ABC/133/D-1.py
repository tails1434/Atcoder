def main():
    N = int(input())
    A = list(map(int, input().split()))

    X1 = 0

    for i in range(N):
        if i % 2 == 0:
            X1 += A[i]
        else:
            X1 -= A[i]

    X = [0] * N
    X[0] = X1
    for i in range(1,N):
        X[i] = 2 * A[i-1] - X[i-1]

    print(*X)



main()