def main():
    N = int(input())
    D, X = map(int, input().split())

    A = [0] * N
    for i in range(N):
        A[i] = int(input())

    cnt = X
    for a in A:
        cnt += 1 + (D - 1) // a

    print(cnt)


main()