def main():
    N, M = map(int, input().split())
    A = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append((a,b))

    sort_A = sorted(A)
    left = 0
    right = N
    cnt = 1
    for i in range(M):
        left = max(sort_A[i][0],left)
        right = min(sort_A[i][1], right)
        if left >= right:
            cnt += 1
            right = sort_A[i][1]

    print(cnt)


    



if __name__ == "__main__":
    main()