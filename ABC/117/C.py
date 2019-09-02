def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))

    if N >= M:
        print(0)
        exit()
    sort_X = sorted(X)
    diff = []
    for i in range(M-1):
        diff.append(sort_X[i+1]-sort_X[i])

    sort_diff = sorted(diff)

    ans = 0
    for i in range(len(sort_diff) - (N - 1)):
        ans += sort_diff[i]

    print(ans)
    

main()