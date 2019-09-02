def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))

    ans = float('inf')
    for i in range(N - K + 1):
        left = x[i]
        right = x[i + K - 1]
        dis = min(abs(left), abs(right)) + right - left
        ans = min(ans, dis)

    print(ans)



main()