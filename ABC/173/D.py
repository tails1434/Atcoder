def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    cnt = 1
    ans = A[0]
    if cnt == N - 1:
        print(ans)
        exit()
    flag = False
    for i in range(1,N):
        if cnt + 1 == N - 1:
            ans += A[i]
            break
        ans += A[i] * 2
        cnt += 2
        if cnt == N - 1:
            break

    print(ans)
    


if __name__ == "__main__":
    main()