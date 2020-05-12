def main():
    N, M, X = map(int, input().split())
    C = [0] * N
    A = [[] for _ in range(N)]
    for i in range(N):
        C[i], *A[i] = map(int, input().split())

    ans = float('inf')
    for i in range(1<<N):
        score = [0] * M
        tmp = []
        money = 0
        for j in range(N):
            if (i >> j) & 1:
                tmp.append(j)
                money += C[j]
        
        for t in tmp:
            for k in range(len(A[t])):
                score[k] += A[t][k]
        flag = True
        for s in score:
            if s < X:
                flag = False

        if flag:
            ans = min(ans, money)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)



if __name__ == "__main__":
    main()