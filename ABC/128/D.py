def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(K+1):
        for r in range(K+1-l):
            if l + r > N:
                continue
            D = K - l - r
            S = []
            now = 0
            for i in range(l):
                now += V[i]
                S.append(V[i])
            for j in range(N-r,N):
                now += V[j]
                S.append(V[j])

            sort_S = sorted(S)
            for d in range(min(D,len(S))):
                if sort_S[d] < 0:
                    now += abs(sort_S[d])

            ans = max(ans, now)

    print(ans)
            

main()