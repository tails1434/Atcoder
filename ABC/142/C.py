def main():
    N = int(input())
    A = list(map(int, input().split()))

    B = []
    for i in range(N):
        B.append([A[i],i+1])

    sort_B = sorted(B)
    ans = []
    for i, j in sort_B:
        ans.append(j)

    print(*ans)
main()