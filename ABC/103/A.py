def main():
    A = list(map(int, input().split()))

    sort_A = sorted(A)
    print(sort_A[2] - sort_A[0])

main()