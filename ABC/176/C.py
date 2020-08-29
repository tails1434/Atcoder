def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for i in range(1,N):
        if A[i-1] <= A[i]:
            continue
        else:
            cnt = A[i-1] - A[i]
            ans += cnt
            A[i] += cnt
    print(ans)

if __name__ == "__main__":
    main()