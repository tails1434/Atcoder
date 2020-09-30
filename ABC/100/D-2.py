def main():
    N, M = map(int, input().split())
    X = [0] * N
    Y = [0] * N
    Z = [0] * N
    for i in range(N):
        X[i], Y[i], Z[i] = map(int, input().split())
    
    ans = 0
    for i in [1,-1]:
        for j in [1,-1]:
            for k in [1,-1]:
                cand = []
                for n in range(N):
                    tmp = i * X[n] + j * Y[n] + k * Z[n]
                    cand.append(tmp)
                cand.sort(reverse=True)
                score = 0
                for m in range(M):
                    score += cand[m]

                ans = max(ans, score)

    print(ans)

if __name__ == "__main__":
    main()