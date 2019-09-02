def main():
    A = list(map(int, input().split()))

    sort_A = sorted(A, reverse=True)
    ans = int(str(sort_A[0]) + str(sort_A[1])) + sort_A[2]
    print(ans)

main()