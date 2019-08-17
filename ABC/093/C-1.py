def main():
    A = list(map(int, input().split()))

    sort_A = sorted(A)

    cnt = 0

    cnt += (sort_A[2] - sort_A[0]) // 2
    sort_A[0] = sort_A[0] + ((sort_A[2] - sort_A[0]) // 2) * 2

    cnt += (sort_A[2] - sort_A[1]) // 2
    sort_A[1] = sort_A[1] + ((sort_A[2] - sort_A[1]) // 2) * 2

    sort_A.sort()
    if sort_A[0] == sort_A[1] == sort_A[2]:
        print(cnt)
    elif sort_A[1] == sort_A[2]:
        print(cnt + 2)
    elif sort_A[0] == sort_A[1]:
        print(cnt + 1)

    

main()