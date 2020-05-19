def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[i+1] = A[i] + B[i]

    ans = 0
    right = 0
    for left in range(N):
        if B[right] - B[left] >= K:
            ans += N - right + 1
            continue
        flag = False
        while True:
            if not flag and right < N:
                right += 1
            tmp = B[right] - B[left]
            if tmp >= K:
                flag = True
                break
            if right == N:
                break
        if flag:
            ans += N - right + 1


    print(ans)

         





if __name__ == "__main__":
    main()