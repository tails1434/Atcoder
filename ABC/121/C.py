def main():
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        a,b = map(int, input().split())
        A.append([a,b])

    sort_A = sorted(A)
    cnt = 0
    money = 0
    for i in range(N):
        if cnt + sort_A[i][1] >= M:
            money += (M - cnt) * sort_A[i][0]
            break
        money += sort_A[i][0] * sort_A[i][1]
        cnt += sort_A[i][1]

    print(money)

main()