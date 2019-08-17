def main():
    A = list(map(int, input().split()))
    K = int(input())

    A[A.index(max(A))] = max(A) * 2 ** K

    print(sum(A))

    


main()