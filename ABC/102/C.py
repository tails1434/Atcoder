from statistics import median

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N

    for i in range(N):
        B[i] = A[i] - i - 1

    b = int(median(B))
    sumB = 0
    for i in range(N):
        sumB += abs(B[i] - b)

    print(sumB)


main()