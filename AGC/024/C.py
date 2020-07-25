def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    if A[0] != 0:
        print(-1)
        exit()
    cnt = A[-1]

    for i in range(N-2,-1,-1):
        if A[i] >= A[i+1]:
            cnt += A[i]
        elif A[i] == A[i+1] - 1:
            continue
        else:
            print(-1)
            exit()

    print(cnt)

if __name__ == "__main__":
    main()