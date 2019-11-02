def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    s = 0
    right = 0
    ans = 0
    for left in range(N):
        while ( right < N and s + A[right] < K):
            s += A[right]
            right += 1
        ans += right - left
        s -= A[left]

    ans = (N * (N + 1)) // 2 - ans
    print(ans)

    
main()