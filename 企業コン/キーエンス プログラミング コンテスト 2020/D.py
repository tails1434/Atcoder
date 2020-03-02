def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [False] * (N - 1)
    D = [False] * (N - 1)
    for i in range(N-1):
        if A[i] <= A[i+1]:
            C[i] = True
        if B[i] >= B[i+1]:
            D[i] = True

    




if __name__ == "__main__":
    main()